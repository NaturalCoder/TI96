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
app.config['SECRET_KEY'] = 'minha_chave_secreta'
bd = SQLAlchemy(app)

class TituloInvalidoError(Exception):
    pass

class ConteudoInvalidoError(Exception):
    pass

class ComentarioVazioError(Exception):
    pass

class Postagem(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    titulo = bd.Column(bd.String(100), nullable=False)
    conteudo = bd.Column(bd.Text, nullable=False)
    criado_em = bd.Column(bd.DateTime, default=datetime.utcnow)
    comentarios = bd.relationship('Comentario', backref='postagem', cascade='all, delete', lazy=True)

    def data_formatada(self):
        return self.criado_em.strftime('%d/%m/%Y')

class Comentario(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    conteudo = bd.Column(bd.Text, nullable=False)
    criado_em = bd.Column(bd.DateTime, default=datetime.utcnow)
    postagem_id = bd.Column(bd.Integer, bd.ForeignKey('postagem.id'), nullable=False)

@app.route('/')
def inicio():
    postagens = Postagem.query.order_by(Postagem.criado_em.desc()).all()
    return render_template('index.html', postagens=postagens)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_postagem():
    if request.method == 'POST':
        try:
            titulo = request.form['titulo']
            conteudo = request.form['conteudo']

            if len(titulo) < 5 or len(titulo) > 100:
                raise TituloInvalidoError("O título deve ter entre 5 e 100 caracteres.")
            if len(conteudo) < 10:
                raise ConteudoInvalidoError("O conteúdo deve ter no mínimo 10 caracteres.")

            nova_postagem = Postagem(titulo=titulo, conteudo=conteudo)
            bd.session.add(nova_postagem)
            bd.session.commit()
            return redirect(url_for('inicio'))

        except (TituloInvalidoError, ConteudoInvalidoError) as erro:
            return render_template('add_post.html', erro=str(erro))
    return render_template('add_post.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    if request.method == 'POST':
        try:
            titulo = request.form['titulo']
            conteudo = request.form['conteudo']

            if len(titulo) < 5 or len(titulo) > 100:
                raise TituloInvalidoError("O título deve ter entre 5 e 100 caracteres.")
            if len(conteudo) < 10:
                raise ConteudoInvalidoError("O conteúdo deve ter no mínimo 10 caracteres.")

            postagem.titulo = titulo
            postagem.conteudo = conteudo
            bd.session.commit()
            return redirect(url_for('inicio'))

        except (TituloInvalidoError, ConteudoInvalidoError) as erro:
            return render_template('edit_post.html', postagem=postagem, erro=str(erro))

    return render_template('edit_post.html', postagem=postagem)

@app.route('/deletar/<int:id>')
def deletar_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    bd.session.delete(postagem)
    bd.session.commit()
    return redirect(url_for('inicio'))

@app.route('/postagem/<int:id>', methods=['GET', 'POST'])
def ver_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    if request.method == 'POST':
        try:
            conteudo = request.form['conteudo']
            if not conteudo.strip():
                raise ComentarioVazioError("O comentário não pode estar vazio.")
            novo_comentario = Comentario(conteudo=conteudo, postagem_id=id)
            bd.session.add(novo_comentario)
            bd.session.commit()
            return redirect(url_for('ver_postagem', id=id))
        except ComentarioVazioError as erro:
            return render_template('ver_postagem.html', postagem=postagem, erro=str(erro))

    return render_template('ver_postagem.html', postagem=postagem)

if __name__ == '__main__':
    with app.app_context():
        bd.create_all()
    app.run(debug=True)