# Importa as funções necessárias do Flask
from flask import Flask, render_template, request, redirect, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Classe que representa uma receita
class Receita:
    def __init__(self, nome):
        self.nome = nome  # Nome da receita
        self.ingredientes = []  # Lista de ingredientes (inicialmente vazia)
        self.modo_preparo = ""  # Modo de preparo (inicialmente vazio)

    # Método para adicionar um ingrediente à receita
    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

# Lista que vai armazenar todas as receitas criadas (em memória)
receitas = []

# Rota principal (página inicial do site)
@app.route('/')
def index():
    # Renderiza a página "index.html"
    return render_template('index.html')

# Rota para cadastro de novas receitas
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    # Se o método for POST, ou seja, o formulário foi enviado
    if request.method == 'POST':
        # Coleta os dados enviados pelo formulário
        nome = request.form['nome'].strip()  # Nome da receita
        ingredientes = request.form['ingredientes'].strip()  # Ingredientes, separados por vírgula
        modo_preparo = request.form['modo_preparo'].strip()  # Modo de preparo

        # Verifica se o nome está vazio
        if not nome:
            # Retorna para o formulário com uma mensagem de erro
            return render_template('cadastrar.html', erro="O nome da receita não pode ser vazio!")

        # Cria um objeto Receita com o nome informado
        receita = Receita(nome)

        # Adiciona os ingredientes (se houver) à receita
        if ingredientes:
            for ing in ingredientes.split(','):
                if ing.strip():  # Ignora espaços em branco
                    receita.adicionar_ingrediente(ing.strip())

        # Atribui o modo de preparo à receita
        receita.modo_preparo = modo_preparo

        # Adiciona a nova receita à lista de receitas
        receitas.append(receita)

        # Redireciona o usuário para a página de listagem
        return redirect(url_for('listar'))

    # Se o método for GET, apenas renderiza a página de cadastro
    return render_template('cadastrar.html')

# Rota para listar todas as receitas cadastradas
@app.route('/listar')
def listar():
    # Renderiza a página de listagem, passando a lista de receitas
    return render_template('listar.html', receitas=receitas)

# Executa o servidor Flask, se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Modo debug ativo (mostra erros detalhados no navegador)
