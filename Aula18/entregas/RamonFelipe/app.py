import os
import re
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# --- Validação de CPF ---
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if digito1 != int(cpf[9]):
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    return digito2 == int(cpf[10])

# --- Exceção personalizada ---
class CPFInvalidoException(Exception):
    pass

# --- App Flask ---
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

LIMITE_POR_TRANSACAO = 5000.00

# --- Models ---
class Usuario(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    gasto_diario = db.Column(db.Float, default=0.0)
    ultima_transacao = db.Column(db.Date)
    chave_aleatoria = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<Usuário {self.nome}>'

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.String(36), db.ForeignKey('usuario.id'), nullable=False)
    destinatario = db.Column(db.String(36), db.ForeignKey('usuario.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    remetente_rel = db.relationship('Usuario', foreign_keys=[remetente])
    destinatario_rel = db.relationship('Usuario', foreign_keys=[destinatario])

with app.app_context():
    db.create_all()

# --- Rotas ---
@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def entrar_usuario():
    if request.method == 'POST':
        chave = request.form.get('cpf')
        chave = chave.strip()

        try:
            if chave.isdigit():
                if not validar_cpf(chave):
                    raise CPFInvalidoException("CPF inválido!")
                usuario = Usuario.query.get(chave)
            else:
                usuario = Usuario.query.filter_by(chave_aleatoria=chave).first()

            if not usuario:
                novo_id = chave if chave.isdigit() else str(uuid4())
                usuario = Usuario(
                    id=novo_id,
                    nome=f"Usuário {novo_id[:8]}",
                    chave_aleatoria=None if chave.isdigit() else chave,
                    saldo=0.0
                )
                db.session.add(usuario)
                db.session.commit()
                flash('Novo usuário criado automaticamente!', 'info')

            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash(f'Bem-vindo(a), {usuario.nome}!', 'sucesso')
            return redirect(url_for('pagina_inicial'))

        except CPFInvalidoException as e:
            flash(str(e), 'erro')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no acesso: {str(e)}', 'erro')

    return render_template('entrar_usuario.html')

@app.route('/logout')
def sair():
    session.clear()
    flash('Você saiu do sistema', 'info')
    return redirect(url_for('pagina_inicial'))

@app.route('/usuarios/novo', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        try:
            cpf = request.form['cpf']
            if not validar_cpf(cpf):
                raise CPFInvalidoException("CPF inválido!")

            novo_usuario = Usuario(
                id=cpf,
                nome=request.form['nome'],
                saldo=float(request.form.get('saldo_inicial', 0)),
                chave_aleatoria=str(uuid4())
            )
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'sucesso')
            return redirect(url_for('pagina_inicial'))
        except CPFInvalidoException as e:
            flash(str(e), 'erro')
        except IntegrityError:
            db.session.rollback()
            flash('Erro: CPF ou chave já cadastrado!', 'erro')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no cadastro: {str(e)}', 'erro')
    return render_template('registrar_usuario.html')

@app.route('/pix', methods=['GET', 'POST'])
def fazer_pix():
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))

    if request.method == 'POST':
        try:
            remetente = session['usuario_id']
            chave_dest = request.form['destinatario'].strip()
            valor = float(request.form['valor'])

            if valor > LIMITE_POR_TRANSACAO:
                raise ValueError(f"Valor excede o limite por transação de R${LIMITE_POR_TRANSACAO:.2f}")

            usuario_envio = Usuario.query.get_or_404(remetente)

            usuario_receb = Usuario.query.get(chave_dest)
            if not usuario_receb:
                usuario_receb = Usuario.query.filter_by(chave_aleatoria=chave_dest).first()
            if not usuario_receb:
                raise ValueError("Destinatário não encontrado!")

            data_atual = datetime.utcnow().date()
            if usuario_envio.ultima_transacao != data_atual:
                usuario_envio.gasto_diario = 0.0

            if usuario_envio.saldo < valor:
                raise ValueError("Saldo insuficiente!")

            usuario_envio.saldo -= valor
            usuario_receb.saldo += valor
            usuario_envio.gasto_diario += valor
            usuario_envio.ultima_transacao = data_atual

            nova_transacao = Transacao(remetente=remetente, destinatario=usuario_receb.id, valor=valor)
            db.session.add(nova_transacao)
            db.session.commit()

            flash('PIX realizado com sucesso!', 'sucesso')
            return redirect(url_for('consultar_saldo'))

        except Exception as e:
            db.session.rollback()
            flash(f'Erro na transação: {str(e)}', 'erro')

    return render_template('fazer_pix.html')

@app.route('/saldo')
def consultar_saldo():
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))

    usuario = Usuario.query.get_or_404(session['usuario_id'])
    return render_template('saldo.html', usuario=usuario)

@app.route('/transacoes')
def historico_transacoes():
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))

    usuario_id = session['usuario_id']
    usuario = Usuario.query.get_or_404(usuario_id)
    transacoes = Transacao.query.filter(
        (Transacao.remetente == usuario_id) |
        (Transacao.destinatario == usuario_id)
    ).order_by(Transacao.data_hora.desc()).all()
    return render_template('transacoes.html', usuario=usuario, transacoes=transacoes)

if __name__ == '__main__':
    app.run(debug=True)
