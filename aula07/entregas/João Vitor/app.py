from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def indice():
    return render_template('index.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')

@app.route('/cadastro')
def cadastro():
    return render_template('02 - JS validação.html')


if __name__ == '__main__':
    app.run(debug=True)