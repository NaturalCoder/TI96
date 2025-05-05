import hashlib

# Texto que será transformado em hash
texto = "Daniel11"

# Criando um hash SHA-256 (pode usar também md5, sha1, sha512, etc.)
hash_obj = hashlib.sha256(texto.encode())

# Obtendo a representação hexadecimal do hash
hash_hex = hash_obj.hexdigest()

print("Hash SHA-256:", hash_hex)