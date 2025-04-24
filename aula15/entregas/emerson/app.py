from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
 
receitas = []
 
@app.route('/')
def listar_receitas():
    return render_template('index.html', receitas=receitas)
 
 
@app.route('/cadastrar')
def cad():
    return render_template('cadastrar.html')
 
 
 
@app.route('/nova', methods=['GET', 'POST'])
def nova_receita():
    if request.method == 'POST':
        nome = request.form['nome']
        ingredientes = request.form.getlist('ingredientes[]')
        id_receita = len(receitas) + 1
        receitas.append({'id': id_receita, 'nome': nome, 'ingredientes': ingredientes})
        return redirect(url_for('listar_receitas'))
    return render_template('nova.html')
 
@app.route('/receita/<int:id>')
def ver_receita(id):
    receita = next((r for r in receitas if r['id'] == id), None)
    if not receita:
        return "Receita não encontrada", 404
    return render_template('detalhes.html', receita=receita)
 
@app.route('/excluir/<int:id>', methods=['POST'])
def excluir_receita(id):
    receitas = [r for r in receitas if r['id'] != id]
    return redirect(url_for('listar_receitas'))
 
 
 
if __name__ == '__main__':
    app.run(debug=True)