from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


alunos = [
    {'id': 1, 'nome': 'João', 'email': 'joao@example.com', 'telefone': '123456789', 'data_nascimento': '2000-01-01'},
    {'id': 2, 'nome': 'Maria', 'email': 'maria@example.com', 'telefone': '987654321', 'data_nascimento': '1999-05-12'}
]

@app.route('/')
def index():
    return render_template('index.html', alunos=alunos)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    
    if not aluno:
        return "Aluno não encontrado", 404

    if request.method == 'POST':
      
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        data_nascimento = request.form.get('data_nascimento')

        
        if not nome or not email or not telefone or not data_nascimento:
            return "Erro: Todos os campos devem ser preenchidos.", 400

        
        aluno['nome'] = nome
        aluno['email'] = email
        aluno['telefone'] = telefone
        aluno['data_nascimento'] = data_nascimento

        return redirect(url_for('index'))  

    return render_template('editar.html', aluno=aluno)

if __name__ == '__main__':
    app.run(debug=True)
