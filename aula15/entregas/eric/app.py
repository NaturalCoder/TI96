from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

receitas = []

@app.route('/')
def index():
    return render_template('index.html',  receitas=receitas)



@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')




@app.route('/listar')
def listar():
    return render_template('listar.html', receitas=receitas)



@app.route('/salvar', methods=['POST'])
def salvar():
    titulo  = request.form['titulo']
    ingredientes = request.form['ingredientes']
    modo_preparo = request.form['modo_preparo']
    tempo = request.form['tempo']

    receita = {
        'titulo': titulo,
        'ingredientes': ingredientes,
        'modo_preparo': modo_preparo,
        'tempo': tempo
    }

    receitas.append(receita) 

    return redirect('/')
    #return f"Receita '{titulo}' cadastrada com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)