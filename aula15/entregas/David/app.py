from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


receitas = []

class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

@app.route('/')
def index():
    return render_template('index.html', receitas=receitas)

@app.route('/nova_receita', methods=['GET', 'POST'])
def nova_receita():
    if request.method == 'POST':
        nome = request.form['nome']
        nova = Receita(nome)

        ingredientes = request.form.getlist('ingredientes')
        for ing in ingredientes:
            if ing.strip():  
                nova.adicionar_ingrediente(ing.strip())

        nova.modo_preparo = request.form['modo_preparo']
        receitas.append(nova)
        return redirect(url_for('index'))

    return render_template('nova_receita.html')

@app.route('/detalhes_receita/<int:receita_id>')
def detalhes_receita(receita_id):
    if 0 <= receita_id < len(receitas):
        receita = receitas[receita_id]
        return render_template('detalhes.html', receita=receita)
    else:
        return "Receita não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)