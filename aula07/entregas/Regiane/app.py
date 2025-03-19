from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/lista.html')
def lista():
    return render_template('tarefas.html')









if __name__ == '__main__':
    app.run(debug=True)
