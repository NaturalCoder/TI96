from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

receitas = []

@app.route('/')
def index():
    return render_template('index.html', receitas=receitas)

@app.route('/nova', methods=['GET', 'POST'])
def nova_receita():
    if request.method == 'POST':
        nome = request.form['nome']
        ingredientes = request.form.getlist('ingredientes')
        modo_preparo = request.form['modo_preparo']

        nova = Receita(nome)
        for ing in ingredientes:
            if ing.strip():
                nova.adicionar_ingrediente(ing)
        nova.modo_preparo = modo_preparo
        receitas.append(nova)

        return redirect(url_for('index'))

    return render_template('nova_receita.html')

@app.route('/detalhes/<int:indice>')
def detalhes(indice):
    if 0 <= indice < len(receitas):
        receita = receitas[indice]
        # Aqui está a correção: passando o índice para o template
        return render_template('detalhes.html', receita=receita, indice=indice)
    return "Receita não encontrada", 404

@app.route('/excluir/<int:indice>', methods=['POST'])
def excluir(indice):
    if 0 <= indice < len(receitas):
        del receitas[indice]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
