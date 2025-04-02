from flask import Flask, render_template
import sqlite3
from contextlib import closing

app = Flask(__name__)

#criar banco
BANCO_DE_DADOS = 'filmes.db'

@app.route('/')
def home():
    #iniciar_banco()
    conexao = conectar_banco()
    
    #selecionar filmes
    """Busca um usuário pelo nome (SELECT)"""
    with closing(conectar_banco()) as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM filmes LIMIT 7')
        filmes = cursor.fetchall()
        return render_template('index.html', filmes=filmes)








def iniciar_banco():
    """Cria o banco de dados e tabela de usuários se não existirem"""
    with closing(sqlite3.connect(BANCO_DE_DADOS)) as conexao:
        with conexao:  # Transação automática
            conexao.execute('''
                CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_do_filme    TEXT UNIQUE NOT NULL,
                    descricao        TEXT UNIQUE NOT NULL,
                    link             TEXT UNIQUE NOT NULL
                )
            ''')
            # Insere usuário admin padrão se a tabela estiver vazia
            if not conexao.execute('SELECT 1 FROM filmes LIMIT 1').fetchone():
                conexao.execute("""INSERT INTO filmes (nome_do_filme, descricao, link) VALUES
('A Cabana', 'O drama, que conta a história de um pai que lida com o desaparecimento da filha, é de tom espiritual e foi baseado em um dos maiores best-sellers mundiais. A Cabana conta a história de Mackenzie Allen Phillips, um homem atormentado pelo sumiço de sua filha mais nova.', 'https://www.youtube.com/watch?v=bk2YojyyCjc'),
('A Espera de um Milagre', 'Milagres acontecem em lugares inesperados, mesmo no bloco de celas para o corredor da morte na Penitenciária Cold Mountain. Lá, John Coffey, um gentil e gigante prisioneiro com poderes sobrenaturais, traz um senso de espírito e humanidade aos seus guardas e colegas de cela.', 'https://www.youtube.com/watch?v=pDJ018gxKPM&list=PLA3txpxkJBG2pfUflvIjTg8nsgydkAdu9'),
('Shrek 2', 'Shrek e Fiona acabaram de voltar da lua de mel e vivem felizes em sua casa no pântano. O casal recebe um convite dos pais da princesa, que querem conhecer o novo genro, para um jantar no castelo. Eles ficaram sabendo que Fiona havia se casado com o seu verdadeiro amor, mas o que eles ainda não sabem é que este amor é um ogro mal-educado de mais de 300 quilos, que conta com um burro falante como melhor amigo.', 'https://www.youtube.com/watch?v=bbwNoCT499Y&list=PLVpkRH8pEby02whOpejuF46w3OsVJ6LEE'),
('Passe Livre', 'Os melhores amigos Rick e Fred estão casados há muito tempo e tentam revitalizar seus casamentos quando recebem permissão de suas esposas para fazer o que quiserem durante uma semana. A princípio, os amigos acreditam que estão prestes a realizar um sonho, mas, aos poucos, percebem que suas expectativas não coincidem com a realidade.', 'https://www.youtube.com/watch?v=m6EkNNHFt3c'),
('Velozes e Furiosos', 'Brian OConner é um policial que se infiltra no submundo dos rachas de rua para investigar uma série de furtos. Enquanto tenta ganhar o respeito e a confiança do líder Dom Toretto, ele corre o risco de ser desmascarado.', 'https://www.youtube.com/watch?v=GGdWwCcC07w'),
('Uma Linda Mulher', 'Executivo milionário e solitário contrata uma jovem prostituta para lhe fazer companhia por uma semana. Aos poucos, ele se encanta e fica apaixonado pela mulher.', 'https://www.youtube.com/watch?v=Qq-MbAo2Y5o&list=PLjcnr0i_Iou4NyIysu8fn6i8dxgdBKOzz&index=2'),
('Jogos Mortais', 'Jigsaw é um assassino que possui uma marca registrada: ele deixa em suas vítimas uma cicatriz em forma de quebra-cabeças, que faz com que elas cometam atos ignóbeis para se salvar. O detetive David Tapp (Danny Glover) é designado para investigar os assassinatos, bem como a capturar seu autor.', 'https://www.youtube.com/watch?v=52zDaVK8-58&list=PLvPF8907fdZNpGnrT2qeyP8XEr66TKhcP');
""")
                


def conectar_banco():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect(BANCO_DE_DADOS)






    # atribuir variaveis


    return render_template('index.html')












app.run(debug=True)