# Função para validar CPF
def validar_cpf(cpf):
    """Valida se o CPF é válido usando o algoritmo de verificação de dígitos."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11:  # Verifica se o CPF tem 11 dígitos
        return False
    if cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais (exemplo: 111.111.111-11)
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):  # Verifica o primeiro dígito verificador
        return False
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):  # Verifica o segundo dígito verificador
        return False
    
    return True


from algosdk import account

def gerar_chaves():
    """
    Gera um par de chaves (chave privada e endereço público) usando a biblioteca algosdk.
    
    Returns:
        tuple: Chave privada e endereço público
    """
    
    # Gerar par de chaves
    private_key, public_address = account.generate_account()

    #print("Chave Privada:", private_key)
    #print("Endereço Público (Chave Pública):", public_address)
    
    return private_key, public_address

