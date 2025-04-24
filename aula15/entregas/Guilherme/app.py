from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Classe para representar uma receita
class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

# Lista para armazenar as receitas cadastradas
receitas = []

# Rota principal (menu inicial)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para cadastrar uma nova receita
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome'].strip()
        ingredientes = request.form['ingredientes'].strip()
        modo_preparo = request.form['modo_preparo'].strip()
        
        # Validações
        if not nome:
            return render_template('cadastrar.html', erro="O nome da receita não pode ser vazio!")
        
        # Cria a receita e adiciona os ingredientes
        receita = Receita(nome)
        if ingredientes:
            for ing in ingredientes.split(','):
                if ing.strip():
                    receita.adicionar_ingrediente(ing.strip())
        receita.modo_preparo = modo_preparo
        
        # Adiciona a receita à lista
        receitas.append(receita)
        return redirect(url_for('listar'))
    
    return render_template('cadastrar.html')

# Rota para listar as receitas cadastradas
@app.route('/listar')
def listar():
    return render_template('listar.html', receitas=receitas)

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)