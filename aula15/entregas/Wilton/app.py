from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Classe Receita
class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = []

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def adicionar_modo_preparo(self, etapa):
        self.modo_preparo.append(etapa)

    def exibir_receita(self):
        return {"nome": self.nome, "ingredientes": self.ingredientes, "modo_preparo": self.modo_preparo}

# Classe Menu
class Menu:
    def __init__(self):
        self.receitas = []

    def cadastrar_receita(self, nome, ingredientes, modo_preparo):
        receita = Receita(nome)
        for ingrediente in ingredientes:
            receita.adicionar_ingrediente(ingrediente)
        for etapa in modo_preparo:
            receita.adicionar_modo_preparo(etapa)
        self.receitas.append(receita)

    def listar_receitas(self):
        return [receita.nome for receita in self.receitas]

    def buscar_receita(self, nome):
        nome_normalizado = nome.strip().lower()
        for receita in self.receitas:
            if receita.nome.strip().lower() == nome_normalizado:
                return receita
        return None

    def excluir_receita(self, nome):
        # Verifica se a receita existe
        receita = self.buscar_receita(nome)
        if receita:
            self.receitas.remove(receita)  # Remove a receita da lista
            return True
        else:
            print(f"Receita '{nome}' não encontrada.")  # Log de erro caso a receita não seja encontrada
            return False

# Instância de Menu
menu = Menu()

@app.route('/')
def home():
    return render_template('index.html', receitas=menu.listar_receitas())

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        
        # Recebe os ingredientes e modo de preparo como listas
        ingredientes = request.form.getlist('ingredientes')
        modo_preparo = request.form.getlist('modo_preparo')
        
        menu.cadastrar_receita(nome, ingredientes, modo_preparo)
        return redirect(url_for('home'))
    return render_template('cadastrar.html')

@app.route('/receita/<nome>')
def receita(nome):
    receita = menu.buscar_receita(nome)
    if receita:
        return render_template('receita.html', receita=receita)
    else:
        return f"Receita {nome} não encontrada!", 404

@app.route('/excluir/<nome>', methods=['POST', 'GET'])
def excluir(nome):
    if menu.excluir_receita(nome):
        return redirect(url_for('home'))  # Redireciona após exclusão
    else:
        return f"Receita '{nome}' não encontrada!", 404  # Exibe mensagem se não encontrada

if __name__ == '__main__':
    app.run(debug=True)
