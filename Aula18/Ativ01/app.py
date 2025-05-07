"""
Ativ 01 - Dada a aplicação Envio PIX
    Corrija todos os BUGs
    Modifique a aplicação para aceitar chave aleatória
    Lance a exceção personalizada quando necessário
    Valide o CPF
    Melhore o visual e utilidade da aplicação

"""
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Configuração inicial do Flask
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Constantes do sistema
LIMITE_POR_TRANSACAO = 5000.00  # R$5.000,00

# Modelagem do banco de dados
class Usuario(db.Model):
    """
    Representa um usuário do sistema PIX
    Campos:
    - id: CPF ou identificador único (string)
    - nome: Nome completo do usuário
    - saldo: Saldo atual da conta
    - gasto_diario: Total movimentado no dia
    - ultima_transacao: Data da última transação
    """
    id = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    gasto_diario = db.Column(db.Float, default=0.0)
    ultima_transacao = db.Column(db.Date)

    def __repr__(self):
        return f'<Usuário {self.nome}>'

class Transacao(db.Model):
    """
    Registro de transações PIX
    Campos:
    - id: Número único da transação
    - remetente: ID do usuário que enviou
    - destinatario: ID do usuário que recebeu
    - valor: Quantia transferida
    - data_hora: Timestamp da transação
    """
    id = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)
    destinatario = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    remetente_rel = db.relationship('Usuario', foreign_keys=[remetente])
    destinatario_rel = db.relationship('Usuario', foreign_keys=[destinatario])

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rotas da aplicação
@app.route('/')
def pagina_inicial():
    """Página inicial com menu de opções"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def entrar_usuario():
    """Autentica ou cria um usuário e inicia a sessão"""
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        
        try:
            # Remove caracteres não numéricos
            cpf = ''.join(filter(str.isdigit, cpf))
            
            # Verifica se o usuário já existe
            usuario = Usuario.query.get(cpf)
            
            if not usuario:
                # Cria novo usuário se não existir
                usuario = Usuario(
                    id=cpf,
                    nome=f"Usuário {cpf}",
                    saldo=0.0
                )
                db.session.add(usuario)
                db.session.commit()
                flash('Novo usuário criado automaticamente!', 'info')
            
            # Inicia sessão
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
        try:
            novo_usuario = Usuario(
                id=request.form['cpf'],
                nome=request.form['nome'],
                saldo=float(request.form.get('saldo_inicial', 0))
            )
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'sucesso')
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
            # Coleta dados do formulário
            remetente = session['usuario_id'] # Usuário logado é o remetente
            destinatario = request.form['destinatario']
            valor = float(request.form['valor'])
            
            # Validações iniciais
            if valor > LIMITE_POR_TRANSACAO:
                raise ValueError(f"Valor excede o limite por transação de R${LIMITE_POR_TRANSACAO}")
                
            # Busca usuários no banco
            usuario_envio = Usuario.query.get_or_404(remetente)
            usuario_receb = Usuario.query.get_or_404(destinatario)
            
            # Verifica limite diário
            data_atual = datetime.utcnow().date()
            if usuario_envio.ultima_transacao != data_atual:
                usuario_envio.gasto_diario = 0.0
                
            #if (usuario_envio.gasto_diario + valor) > LIMITE_DIARIO:
            #    raise ValueError(f"Limite diário de R${LIMITE_DIARIO} atingido!")
            
            # Verifica saldo
            if usuario_envio.saldo < valor:
                raise ValueError("Saldo insuficiente!")
            
            # Atualiza saldos
            usuario_envio.saldo -= valor
            usuario_receb.saldo += valor
            usuario_envio.gasto_diario += valor
            usuario_envio.ultima_transacao = data_atual
            
            # Registra transação
            nova_transacao = Transacao(
                remetente=remetente,
                destinatario=destinatario,
                valor=valor
            )
            db.session.add(nova_transacao)
            db.session.commit()
            
            flash('PIX realizado com sucesso!', 'sucesso')
            return redirect(url_for('consultar_saldo', usuario_id=remetente))
            
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

@app.route('/transacoes')
def historico_transacoes(usuario_id):
    """Mostra histórico completo de transações"""
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))
    
    usuario = Usuario.query.get_or_404(session['usuario_id'])
    transacoes = Transacao.query.filter(
        (Transacao.remetente == usuario_id) | 
        (Transacao.destinatario == usuario_id)
    ).order_by(Transacao.data_hora.desc()).all()
    return render_template('transacoes.html', usuario=usuario, transacoes=transacoes)

if __name__ == '__main__':
    app.run(debug=True)