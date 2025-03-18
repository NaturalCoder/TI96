from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def indice():
    return render_template('index.html')

@app.route('/tarefass')
def link1():
    return render_template('tarefas.html')

@app.route('/cadastroo')
def link2():
    return render_template('02 - JS validação.html')

if __name__ == '__main__':
    app.run(debug=True)