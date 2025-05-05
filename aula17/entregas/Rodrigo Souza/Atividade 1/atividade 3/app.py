"""
Ativ 03 – Dada a aplicação Mural implemente melhorias:
Valide o tamanho dos campos (usando exceções)
Melhore a formatação da data da postagem
Melhore o visual, mude cores, tamanhos, etc.
Implemente uma funcionalidade da sua escolha.
"""
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'posts.db')
app.config['SECRET_KEY'] = 'sua_chave_secreta'
bd = SQLAlchemy(app)

class Postagem(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    titulo = bd.Column(bd.String(100), nullable=False)
    conteudo = bd.Column(bd.Text, nullable=False)
    criado_em = bd.Column(bd.DateTime, default=datetime.utcnow)

@app.route('/')
def inicio():
    postagens = Postagem.query.order_by(Postagem.criado_em.desc()).all()
    return render_template('index.html', postagens=postagens)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_postagem():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        nova_postagem = Postagem(titulo=titulo, conteudo=conteudo)
        bd.session.add(nova_postagem)
        bd.session.commit()
        return redirect(url_for('inicio'))
    return render_template('add_post.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    if request.method == 'POST':
        postagem.titulo = request.form['titulo']
        postagem.conteudo = request.form['conteudo']
        bd.session.commit()
        return redirect(url_for('inicio'))
    return render_template('edit_post.html', postagem=postagem)

@app.route('/deletar/<int:id>')
def deletar_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    bd.session.delete(postagem)
    bd.session.commit()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    with app.app_context():
        bd.create_all()
    app.run(debug=True)