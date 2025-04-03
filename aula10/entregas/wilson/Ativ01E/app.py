# AES-256 com Flask usando cryptography

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3, os, datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# Caminho da chave
key_path = "chave_aes256.key"

# Gera e salva a chave se não existir
if not os.path.exists(key_path):
    key = AESGCM.generate_key(bit_length=256)
    with open(key_path, "wb") as f:
        f.write(key)
    print("✅ Chave AES-256 criada com sucesso.")
else:
    print("🔑 Chave AES-256 carregada.")

# Carrega a chave
def load_key():
    with open(key_path, "rb") as f:
        return f.read()

key = load_key()
aesgcm = AESGCM(key)

# Banco de dados
def init_db():
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
    )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS senhas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        tipo TEXT,
        site TEXT,
        username TEXT,
        password BLOB,
        nonce BLOB,
        data_criacao DATE
    )"""
    )
    conn.commit()
    conn.close()

init_db()

# Cadastro
@app.route("/api/auth/register", methods=["POST"])
def register():
    data = request.json
    email = data["email"]
    password = generate_password_hash(data["password"])
    try:
        conn = sqlite3.connect("senhas.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (email, password) VALUES (?, ?)", (email, password)
        )
        conn.commit()
        return jsonify({"message": "Usuário registrado."})
    except sqlite3.IntegrityError:
        return jsonify({"message": "E-mail já cadastrado."}), 400
    finally:
        conn.close()

# Login
@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    senha = data["password"]
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM usuarios WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[1], senha):
        return jsonify({"message": "Login bem-sucedido", "userId": user[0]})
    return jsonify({"message": "Credenciais inválidas"}), 401

""" # Salvar senha criptografada com regras
@app.route("/api/passwords/<int:id>", methods=["DELETE"])
def mover_para_lixeira(id):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE senhas SET deletado = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Movido para a lixeira com sucesso."}) """

@app.route("/api/lixeira/<int:user_id>", methods=["GET"])
def listar_lixeira(user_id):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, tipo, site, username, password, nonce, data_criacao
        FROM senhas
        WHERE user_id = ? AND deletado = 1
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()

    resultado = []
    for id_, tipo, site, username, senha_cript, nonce, data in rows:
        senha = aesgcm.decrypt(nonce, senha_cript, None).decode()
        resultado.append({
            "id": id_,
            "tipo": tipo,
            "site": site,
            "username": username,
            "password": senha,
            "data": data
        })

    return jsonify(resultado)

@app.route("/api/lixeira/restaurar/<int:id>", methods=["PUT"])
def restaurar_senha(id):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE senhas SET deletado = 0 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Senha restaurada com sucesso."})



@app.route("/api/passwords", methods=["POST"])
def salvar():
    data = request.json
    user_id = data["user_id"]
    tipo = data["tipo"]
    site = data["site"]
    username = data["username"]
    senha = data["password"]

    # Verifica força da senha
    if (
        len(senha) < 12
        or not any(c.isdigit() for c in senha)
        or not any(c.isalpha() for c in senha)
        or not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in senha)
    ):
        return (
            jsonify(
                {
                    "message": "Senha deve conter mais de 12 caracteres, letras, números e símbolos."
                }
            ),
            400,
        )

    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()

    # Verifica se senha já foi usada nos últimos 120 dias
    cursor.execute(
        "SELECT password, nonce, data_criacao FROM senhas WHERE user_id = ?", (user_id,)
    )
    for s_cript, nonce, data in cursor.fetchall():
        try:
            senha_anterior = aesgcm.decrypt(nonce, s_cript, None).decode()
            if senha_anterior == senha:
                dias = (datetime.date.today() - datetime.date.fromisoformat(data)).days
                if dias <= 120:
                    return (
                        jsonify(
                            {"message": "Senha já utilizada nos últimos 120 dias."}
                        ),
                        400,
                    )
        except:
            continue

    nonce = os.urandom(12)
    senha_cript = aesgcm.encrypt(nonce, senha.encode(), None)
    data_criacao = datetime.date.today().isoformat()

    cursor.execute(
        "INSERT INTO senhas (user_id, tipo, site, username, password, nonce, data_criacao) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (user_id, tipo, site, username, senha_cript, nonce, data_criacao),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Senha salva com AES-256"})

# Listar senhas descriptografadas
@app.route("/api/passwords/<int:user_id>", methods=["GET"])
def listar(user_id):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT s.tipo, s.site, s.username, s.password, s.nonce, s.data_criacao, u.email
        FROM senhas s
        JOIN usuarios u ON s.user_id = u.id
        WHERE s.user_id = ?
    """,
        (user_id,),
    )
    rows = cursor.fetchall()
    conn.close()

    resultado = []
    for tipo, site, username, senha_cript, nonce, data, email in rows:
        senha = aesgcm.decrypt(nonce, senha_cript, None).decode()
        dias = (datetime.date.today() - datetime.date.fromisoformat(data)).days
        trocar = dias >= 30
        resultado.append(
            {
                "tipo": tipo,
                "site": site,
                "username": username,
                "email": email,
                "password": senha,
                "data": data,
                "dias": dias,
                "trocar": trocar,
            }
        )

    return jsonify(resultado)

# Novo: Relatório completo
@app.route("/api/relatorio/<int:user_id>", methods=["GET"])
def relatorio(user_id):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT tipo, site, username, data_criacao FROM senhas WHERE user_id = ? ORDER BY data_criacao DESC",
        (user_id,),
    )
    rows = cursor.fetchall()
    conn.close()

    relatorio = []
    for tipo, site, username, data in rows:
        dias = (datetime.date.today() - datetime.date.fromisoformat(data)).days
        relatorio.append(
            {
                "tipo": tipo,
                "site": site,
                "username": username,
                "data_criacao": data,
                "dias_desde_criacao": dias,
                "status_troca": "Recomendada" if dias >= 30 else "Ok",
            }
        )

    return jsonify(relatorio)

# Rotas de páginas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)