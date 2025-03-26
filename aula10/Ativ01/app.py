# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from contextlib import closing

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessária para sessões seguras

# Configuração do banco de dados
BANCO_DE_DADOS = 'usuarios.db'

def iniciar_banco():
    """Cria o banco de dados e tabela de usuários se não existirem"""
    with closing(sqlite3.connect(BANCO_DE_DADOS)) as conexao:
        with conexao:  # Transação automática
            conexao.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')
            # Insere usuário admin padrão se a tabela estiver vazia
            if not conexao.execute('SELECT 1 FROM usuarios LIMIT 1').fetchone():
                conexao.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', 
                              ('admin', 'secret'))

def conectar_banco():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect(BANCO_DE_DADOS)

# Funções de operações no banco (CRUD)
def buscar_usuario(usuario):
    """Busca um usuário pelo nome (SELECT)"""
    with closing(conectar_banco()) as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,))
        return cursor.fetchone()

def criar_usuario(usuario, senha):
    """Exemplo: Insere novo usuário (INSERT)"""
    try:
        with closing(conectar_banco()) as conexao:
            conexao.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', 
                          (usuario, senha))
            return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe

def atualizar_senha(usuario, nova_senha):
    """Exemplo: Atualiza senha do usuário (UPDATE)"""
    with closing(conectar_banco()) as conexao:
        with conexao:
            conexao.execute('UPDATE usuarios SET senha = ? WHERE usuario = ?',
                          (nova_senha, usuario))
            return conexao.total_changes > 0

# Rotas
@app.route('/')
def inicio():
    """Redireciona para a página de login"""
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Processa o formulário de login"""
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        usuario_db = buscar_usuario(usuario)
        
        # Verifica credenciais
        if usuario_db and usuario_db[2] == senha:  # usuario_db[2] = campo senha
            session['usuario_logado'] = usuario
            return redirect(url_for('sucesso'))
        else:
            flash('Usuário ou senha incorretos!', 'erro')
    
    return render_template('login.html')

@app.route('/sucesso')
def sucesso():
    """Página restrita após login"""
    if 'usuario_logado' not in session:
        flash('Faça login primeiro!', 'erro')
        return redirect(url_for('login'))
    return render_template('sucesso.html')

@app.route('/logout')
def logout():
    """Encerra a sessão do usuário"""
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

# Inicializa o banco quando o app iniciar
with app.app_context():
    iniciar_banco()

if __name__ == '__main__':
    app.run(debug=True)