import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


LIMITE_POR_TRANSACAO = 5000.00  

# 
class SaldoInsuficienteException(Exception):
    pass


class Usuario(db.Model):
    """
    Representa um usuário do sistema PIX
    Campos:
    - id: CPF ou identificador único (string)
    - nome: Nome completo do usuário
    - saldo: Saldo atual da conta
    - gasto_diario: Total movimentado no dia
    - ultima_transacao: Data da última transação
    - chave_pix: Chave aleatória do usuário
    """
    id = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    gasto_diario = db.Column(db.Float, default=0.0)
    ultima_transacao = db.Column(db.Date)
    chave_pix = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuário {self.nome}>'

    @staticmethod
    def gerar_chave_aleatoria():
        """Gera uma chave aleatória para o usuário"""
        return f'{datetime.utcnow().strftime("%Y%m%d%H%M%S%f")[:16]}'

class Transacao(db.Model):
    """
    Registro de transações PIX
    """
    id = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)
    destinatario = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)

    remetente_rel = db.relationship('Usuario', foreign_keys=[remetente])
    destinatario_rel = db.relationship('Usuario', foreign_keys=[destinatario])


with app.app_context():
    db.create_all()


def validar_cpf(cpf):
    """Valida o CPF usando a regra básica do CPF"""
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    
    return True


@app.route('/')
def pagina_inicial():
    """Página inicial com menu de opções"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def entrar_usuario():
    """Autentica ou cria um usuário e inicia a sessão"""
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        
        if not validar_cpf(cpf):
            flash('CPF inválido!', 'erro')
            return redirect(url_for('entrar_usuario'))

        try:
            
            cpf = ''.join(filter(str.isdigit, cpf))
            
            
            usuario = Usuario.query.get(cpf)
            
            if not usuario:
                
                chave_pix = Usuario.gerar_chave_aleatoria()
                usuario = Usuario(
                    id=cpf,
                    nome=f"Usuário {cpf}",
                    saldo=0.0,
                    chave_pix=chave_pix
                )
                db.session.add(usuario)
                db.session.commit()
                flash(f'Novo usuário criado automaticamente! Sua chave PIX é: {chave_pix}', 'info')
            
            
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash(f'Bem-vindo(a), {usuario.nome}!', 'sucesso')
            return redirect(url_for('pagina_inicial'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no acesso: {str(e)}', 'erro')
    
    return render_template('entrar_usuario.html')

@app.route('/logout')
def sair():
    """Encerra a sessão do usuário"""
    session.clear()
    flash('Você saiu do sistema', 'info')
    return redirect(url_for('pagina_inicial'))

@app.route('/usuarios/novo', methods=['GET', 'POST'])
def registrar_usuario():
    """Cadastra novo usuário no sistema"""
    if request.method == 'POST':
        cpf = request.form['cpf']
        
        if not validar_cpf(cpf):
            flash('CPF inválido!', 'erro')
            return redirect(url_for('registrar_usuario'))

        try:
            chave_pix = Usuario.gerar_chave_aleatoria()
            novo_usuario = Usuario(
                id=cpf,
                nome=request.form['nome'],
                saldo=float(request.form.get('saldo_inicial', 0)),
                chave_pix=chave_pix
            )
            db.session.add(novo_usuario)
            db.session.commit()
            flash(f'Usuário cadastrado com sucesso! Sua chave PIX é: {chave_pix}', 'sucesso')
            return redirect(url_for('pagina_inicial'))
        except IntegrityError:
            db.session.rollback()
            flash('Erro: CPF já cadastrado!', 'erro')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no cadastro: {str(e)}', 'erro')
    return render_template('registrar_usuario.html')

@app.route('/pix', methods=['GET', 'POST'])
def fazer_pix():
    """Realiza transferência PIX entre usuários"""

    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))
    
    if request.method == 'POST':
        try:
           
            remetente = session['usuario_id'] 
            destinatario = request.form['destinatario']
            valor = float(request.form['valor'])
            
            
            if valor > LIMITE_POR_TRANSACAO:
                raise ValueError(f"Valor excede o limite por transação de R${LIMITE_POR_TRANSACAO}")
                
            
            usuario_envio = Usuario.query.get_or_404(remetente)
            usuario_receb = Usuario.query.get_or_404(destinatario)
            
            
            if usuario_envio.saldo < valor:
                raise SaldoInsuficienteException("Saldo insuficiente!")
            
            
            usuario_envio.saldo -= valor
            usuario_receb.saldo += valor
            usuario_envio.gasto_diario += valor
            usuario_envio.ultima_transacao = datetime.utcnow().date()
            
            
            nova_transacao = Transacao(
                remetente=remetente,
                destinatario=destinatario,
                valor=valor
            )
            db.session.add(nova_transacao)
            db.session.commit()
            
            flash('PIX realizado com sucesso!', 'sucesso')
            return redirect(url_for('consultar_saldo', usuario_id=remetente))
            
        except SaldoInsuficienteException as e:
            db.session.rollback()
            flash(f'Erro na transação: {str(e)}', 'erro')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro na transação: {str(e)}', 'erro')
    
    return render_template('fazer_pix.html')

@app.route('/saldo')
def consultar_saldo():
    """Exibe saldo e limites do usuário"""
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))
    
    usuario = Usuario.query.get_or_404(session['usuario_id'])
    return render_template('saldo.html', usuario=usuario)

@app.route('/transacoes)')