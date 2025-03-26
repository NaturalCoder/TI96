# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from contextlib import closing

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Chave necessária para sessões seguras

# Configuração do banco de dados
DATABASE = 'usuarios.db'

def init_db():
    """Inicializa o banco de dados e cria tabela de usuários"""
    with closing(sqlite3.connect(DATABASE)) as conn:
        with conn:  # Usa transação automaticamente
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')
            # Insere usuário padrão se a tabela estiver vazia
            if not conn.execute('SELECT 1 FROM usuarios LIMIT 1').fetchone():
                conn.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', 
                            ('admin', 'secret'))

def get_db():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect(DATABASE)

# Funções de operações no banco (CRUD)
def get_user_by_username(usuario):
    """Busca usuário pelo nome (SELECT)"""
    with closing(get_db()) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,))
        return cursor.fetchone()

def create_user(usuario, senha):
    """Exemplo de função para inserir novo usuário (INSERT)"""
    try:
        with closing(get_db()) as conn:
            conn.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', 
                       (usuario, senha))
            return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe

def update_user_password(usuario, nova_senha):
    """Exemplo de função para atualizar senha (UPDATE)"""
    with closing(get_db()) as conn:
        with conn:
            conn.execute('UPDATE usuarios SET senha = ? WHERE usuario = ?',
                       (nova_senha, usuario))
            return conn.total_changes > 0

# Rotas
@app.route('/')
def home():
    """Redireciona para a página de login"""
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Gerencia o processo de login"""
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        user = get_user_by_username(usuario)
        
        # Verifica se usuário existe e a senha confere
        if user and user[2] == senha:  # user[2] = campo senha
            session['usuario_logado'] = usuario
            return redirect(url_for('sucesso'))
        else:
            flash('Usuário ou senha incorretos!', 'error')
    
    return render_template('login.html')

@app.route('/sucesso')
def sucesso():
    """Página restrita após login bem-sucedido"""
    if 'usuario_logado' not in session:
        flash('Faça login primeiro!', 'error')
        return redirect(url_for('login'))
    return render_template('sucesso.html')

@app.route('/logout')
def logout():
    """Encerra a sessão do usuário"""
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

# Executa a inicialização do banco quando o app iniciar
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)