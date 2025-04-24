from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


receitas = []

class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = []

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def adicionar_modo_preparo(self, etapa):
        self.modo_preparo.append(etapa)

@app.route('/')
def index():
    return render_template('index.html', receitas=receitas)

@app.route('/nova', methods=['GET', 'POST'])
def nova_receita():
    if request.method == 'POST':
        nome = request.form['nome']
        ingredientes = request.form.getlist('ingredientes')
        preparo = request.form.getlist('modo_preparo')

        receita = Receita(nome)
        for ing in ingredientes:
            if ing.strip():
                receita.adicionar_ingrediente(ing.strip())
        for etapa in preparo:
            if etapa.strip():
                receita.adicionar_modo_preparo(etapa.strip())

        receitas.append(receita)
        return redirect(url_for('index'))

    return render_template('nova_receita.html')

@app.route('/receita/<int:indice>')
def mostrar_receita(indice):
    if 0 <= indice < len(receitas):
        return render_template('receita_detalhe.html', receita=receitas[indice], indice=indice)
    return "Receita não encontrada", 404

@app.route('/excluir/<int:indice>')
def excluir_receita(indice):
    if 0 <= indice < len(receitas):
        receitas.pop(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
