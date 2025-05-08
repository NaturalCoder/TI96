import hashlib
import time


def validar_cpf(cpf):
    """
    Valida um CPF verificando seu formato e dígitos verificadores.
    
    Args:
        cpf: String contendo o CPF (com ou sem pontuação)
    
    Returns:
        bool: True se o CPF é válido, False caso contrário
    """
    
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos ou se é uma sequência de dígitos iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Verifica o primeiro dígito
    if digito1 != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # Verifica o segundo dígito
    if digito2 != int(cpf[10]):
        return False
    
    return True

def gerar_chave_pix():
    import uuid, hashlib
    return hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()


#def gerar_hash_transacao(remetente, destinatario, valor):
    """
    Gera um hash estilo blockchain (SHA-256 duplo) com base nos dados da transação.
    """
    dados = f"{remetente}{destinatario}{valor}{time.time()}"
    hash_1 = hashlib.sha256(dados.encode()).digest()
    hash_final = hashlib.sha256(hash_1).hexdigest()
    return hash_final


def gerar_hash_transacao(remetente, destinatario, valor):
    """
    Gera um hash estilo blockchain (SHA-256 duplo) com base nos dados da transação.
    """
    dados = f"{remetente}{destinatario}{valor}{time.time()}"
    hash_1 = hashlib.sha256(dados.encode()).digest()
    hash_final = hashlib.sha256(hash_1).hexdigest()
    return hash_final

