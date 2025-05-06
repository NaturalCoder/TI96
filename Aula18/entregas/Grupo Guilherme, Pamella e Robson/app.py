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
app = Flask(__name__)  # Cria uma instância da aplicação Flask
basedir = os.path.abspath(os.path.dirname(__file__))  # Diretório base do aplicativo
app.secret_key = 'sua_chave_secreta_aqui'  # Chave secreta usada para proteger a sessão
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')  # Conexão com o banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações para evitar sobrecarga
db = SQLAlchemy(app)  # Cria uma instância do banco de dados com SQLAlchemy

# Constantes do sistema
LIMITE_POR_TRANSACAO = 5000.00  # Limite para transações PIX: R$5.000,00

# Função para validar CPF
def validar_cpf(cpf):
    """Valida se o CPF é válido usando o algoritmo de verificação de dígitos."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11:  # Verifica se o CPF tem 11 dígitos
        return False
    if cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais (exemplo: 111.111.111-11)
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):  # Verifica o primeiro dígito verificador
        return False
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):  # Verifica o segundo dígito verificador
        return False
    
    return True

# Modelagem do banco de dados
class Usuario(db.Model):
    """
    Representa um usuário do sistema PIX
    """
    id = db.Column(db.String(11), primary_key=True)  # CPF ou identificador único do usuário
    nome = db.Column(db.String(100), nullable=False)  # Nome completo do usuário
    saldo = db.Column(db.Float, default=0.0)  # Saldo atual da conta
    gasto_diario = db.Column(db.Float, default=0.0)  # Total movimentado no dia
    ultima_transacao = db.Column(db.Date)  # Data da última transação

    def __repr__(self):
        return f'<Usuário {self.nome}>'

class Transacao(db.Model):
    """
    Registro de transações PIX
    """
    id = db.Column(db.Integer, primary_key=True)  # ID único da transação
    remetente = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)  # Remetente da transação
    destinatario = db.Column(db.String(11), db.ForeignKey('usuario.id'), nullable=False)  # Destinatário da transação
    valor = db.Column(db.Float, nullable=False)  # Valor transferido
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)  # Data e hora da transação

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
            cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
            
            # Valida o CPF
            if not validar_cpf(cpf):
                raise ValueError("CPF inválido!")
            
            usuario = Usuario.query.get(cpf)  # Busca o usuário no banco de dados
            
            if not usuario:  # Se o usuário não existir, cria um novo
                usuario = Usuario(
                    id=cpf,
                    nome=f"Usuário {cpf}",
                    saldo=0.0
                )
                db.session.add(usuario)
                db.session.commit()
                flash('Novo usuário criado automaticamente!', 'info')
            
            session['usuario_id'] = usuario.id  # Inicia sessão com o ID do usuário
            session['usuario_nome'] = usuario.nome  # Inicia sessão com o nome do usuário
            flash(f'Bem-vindo(a), {usuario.nome}!', 'sucesso')
            return redirect(url_for('pagina_inicial'))
            
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            flash(f'Erro no acesso: {str(e)}', 'erro')
    
    return render_template('entrar_usuario.html')

@app.route('/logout')
def sair():
    """Encerra a sessão do usuário"""
    session.clear()  # Limpa os dados da sessão
    flash('Você saiu do sistema', 'info')
    return redirect(url_for('pagina_inicial'))

@app.route('/usuarios/novo', methods=['GET', 'POST'])
def registrar_usuario():
    """Cadastra novo usuário no sistema"""
    if request.method == 'POST':
        try:
            cpf = request.form['cpf']
            if not validar_cpf(cpf):  # Valida o CPF
                raise ValueError("CPF inválido!")
            
            novo_usuario = Usuario(
                id=cpf,
                nome=request.form['nome'],
                saldo=float(request.form.get('saldo_inicial', 0))  # Obtém o saldo inicial, padrão é 0
            )
            db.session.add(novo_usuario)
            db.session.commit()  # Salva o novo usuário no banco de dados
            flash('Usuário cadastrado com sucesso!', 'sucesso')
            return redirect(url_for('pagina_inicial'))
        except IntegrityError:
            db.session.rollback()  # Reverte em caso de CPF já existente
            flash('Erro: CPF já cadastrado!', 'erro')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no cadastro: {str(e)}', 'erro')
    return render_template('registrar_usuario.html')

@app.route('/deposito', methods=['GET', 'POST'])
def depositar():
    """Permite que o usuário deposite dinheiro na própria conta"""
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))  # Redireciona para login se não estiver autenticado
    
    if request.method == 'POST':
        try:
            valor = float(request.form['valor'])  # Coleta o valor do formulário
            
            if valor <= 0:
                raise ValueError("O valor do depósito deve ser maior que zero!")
            if valor > LIMITE_POR_TRANSACAO:
                raise ValueError(f"Valor excede o limite por depósito de R${LIMITE_POR_TRANSACAO}")
            
            usuario = Usuario.query.get_or_404(session['usuario_id'])  # Busca o usuário logado
            usuario.saldo += valor  # Atualiza o saldo do usuário
            db.session.commit()
            
            flash(f'Depósito de R${valor:.2f} realizado com sucesso!', 'sucesso')
            return redirect(url_for('consultar_saldo'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro no depósito: {str(e)}', 'erro')
    
    return render_template('deposito.html')

@app.route('/pix', methods=['GET', 'POST'])
def fazer_pix():
    """Realiza transferência PIX entre usuários"""
    if 'usuario_id' not in session:
        return redirect(url_for('entrar_usuario'))
    
    if request.method == 'POST':
        try:
            remetente = session['usuario_id']  # O remetente é o usuário logado
            destinatario = request.form['destinatario']
            valor = float(request.form['valor'])
            
            if not validar_cpf(destinatario):  # Valida o CPF do destinatário
                raise ValueError("CPF do destinatário inválido!")
            
            if valor > LIMITE_POR_TRANSACAO:
                raise ValueError(f"Valor excede o limite por transação de R${LIMITE_POR_TRANSACAO}")
                
            usuario_envio = Usuario.query.get_or_404(remetente)  # Busca o remetente
            usuario_receb = Usuario.query.get_or_404(destinatario)  # Busca o destinatário
            
            # Verifica saldo
            if usuario_envio.saldo < valor:
                raise ValueError("Saldo insuficiente!")
            
            usuario_envio.saldo -= valor  # Deduz o valor do saldo do remetente
            usuario_receb.saldo += valor  # Adiciona o valor ao saldo do destinatário
            usuario_envio.gasto_diario += valor  # Atualiza o gasto diário do remetente
            usuario_envio.ultima_transacao = datetime.utcnow().date()  # Atualiza a data da última transação
            
            # Registra a transação
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

@app.route('/transacoes/<usuario_id>')
def historico_transacoes(usuario_id):
    """Exibe o histórico de transações do usuário"""
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    usuario = Usuario.query.get_or_404(session['usuario_id'])
    transacoes = Transacao.query.filter(
        (Transacao.remetente == usuario_id) | (Transacao.destinatario == usuario_id)
    ).order_by(Transacao.data_hora.desc()).all()
    return render_template('transacoes.html', usuario=usuario, transacoes=transacoes)

if __name__ == '__main__':
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração
