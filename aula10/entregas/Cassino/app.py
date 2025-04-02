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
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            # Insere usuário admin padrão se a tabela estiver vazia
            if not conexao.execute('SELECT 1 FROM users LIMIT 1').fetchone():
                conexao.execute('INSERT INTO users (user, password) VALUES (?, ?)',('admin', 'secret'))

def conectar_banco():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect(BANCO_DE_DADOS)

def buscar_usuario(user):
    """Busca um usuário pelo nome (SELECT)"""
    with closing(conectar_banco()) as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM users WHERE user = ?', (user,))
        return cursor.fetchone()

def criar_usuario(user, password):
    """Exemplo: Insere novo usuário (INSERT)"""
    try:
        with closing(conectar_banco()) as conexao:
            conexao.execute('INSERT INTO users (user, password) VALUES (?, ?)',
                          (user, password))
            return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe

def atualizar_senha(user, new_password):
    """Exemplo: Atualiza senha do usuário (UPDATE)"""
    with closing(conectar_banco()) as conexao:
        with conexao:
            conexao.execute('UPDATE users SET password = ? WHERE user = ?',
                          (new_password, user))
            return conexao.total_changes > 0

@app.route('/')
def inicio():
    if 'username' not in session:
        return redirect("login")
    else:   
        return render_template('index.html', user = session['username'])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': #recebendo form de login p processar
        user = request.form['user']
        password = request.form['password']
        botao = request.form['botao']
        
        if botao == "entrar":
            user_db = buscar_usuario(user)

            if user_db and user_db[2] == password:
                session['username'] = user
                return redirect('/')
            else:
                flash('Usuário ou senha incorretos!', 'erro')
                return redirect('login')
            
        elif botao == "registrar":
            try:
                with closing(conectar_banco()) as conexao:
                    conexao.execute('INSERT INTO users (user, password) VALUES (?, ?)',(user, password))
                    conexao.commit()
            except sqlite3.IntegrityError:
                flash("Usuario Repetido!!!", "erro")
                return redirect('login')

        flash('Registrado com sucesso!!!', 'sucesso')
        return redirect('/')
            

    else: #mostrando form de login# conasultar no banc
        return render_template('login.html')

with app.app_context():
    iniciar_banco()
 

if __name__ == '__main__':
    app.run(debug=True)