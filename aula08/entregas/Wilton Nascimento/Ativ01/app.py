# app.py
# Importações necessárias
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# 1. CONFIGURAÇÃO INICIAL DA APLICAÇÃO
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações de modificação
db = SQLAlchemy(app)

# 2. DEFINIÇÃO DO MODELO DE DADOS
class Aluno(db.Model):
    # Nomes das colunas em português para facilitar o entendimento
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    idade = db.Column(db.Integer, nullable=True)
    pontos = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f'<Aluno {self.nome}>'

# Cria as tabelas no banco de dados (executar apenas uma vez)
with app.app_context():
    db.create_all()

# 3. DEFINIÇÃO DAS ROTAS E FUNCIONALIDADES

# Rota principal - Listagem de alunos
@app.route('/')
def listar_alunos():
    # Consulta todos os alunos no banco de dados
    alunos = Aluno.query.all()
    return render_template('index.html', alunos=alunos)

# Rota para cadastro de novos alunos
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        # Coleta dados do formulário
        novo_aluno = Aluno(
            nome=request.form['nome'],
            email=request.form['email'],
            idade=request.form['idade'],
            pontos=request.form['pontos']
        )
        
        try:
            db.session.add(novo_aluno)
            db.session.commit()
            return redirect(url_for('listar_alunos'))
        except:
            return 'Erro ao cadastrar aluno!'
    else:
        return render_template('cadastrar.html')

# Rota para edição de alunos
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    
    if request.method == 'POST':
        # Atualiza os dados do aluno
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.idade = request.form['idade']
        aluno.pontos = request.form['pontos']
        
        try:
            db.session.commit()
            return redirect(url_for('listar_alunos'))
        except:
            return 'Erro ao atualizar aluno!'
    else:
        return render_template('editar.html', aluno=aluno)

# Rota para exclusão de alunos
@app.route('/excluir/<int:id>')
def excluir_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    
    try:
        db.session.delete(aluno)
        db.session.commit()
        return redirect(url_for('listar_alunos'))
    except:
        return 'Erro ao excluir aluno!'

if __name__ == '__main__':
    app.run(debug=True)