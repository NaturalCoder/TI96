from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello, Turma!'


@app.route('/user/<nome>')
def user(nome):
    return render_template('index.html', nome=nome)
    


if __name__ == '__main__':
    app.run(debug=True)