# rodar pip install py-algorand-sdk
from algosdk import account, encoding, client, transaction

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

def endereco_eh_valido(address):
    """
    Verifica se um endereço é válido usando a biblioteca algosdk.
    
    Args:
        address: String contendo o endereço a ser verificado
    
    Returns:
        bool: True se o endereço é válido, False caso contrário
    """
    
    try:
        # Verifica se o endereço é válido
        return encoding.is_valid_address(address)
    except Exception as e:
        #print(f"Erro ao verificar o endereço: {e}")
        return False

def enviar_algos(algos:int, destino:str, private_key:str):
    """
    Transmite uma transação para a rede Algorand.
    
    Args:
        algos: Quantidade de ALGOs a serem enviados (em microALGOs)
            1 ALGO = 1.000.000 microALGOs
        destino: Endereço público do destinatário
        private_key: Chave privada do remetente

    """

    # Parâmetros da rede
    params = client.suggested_params()

    # Transação de transferência de ALGOs
    txn = transaction.PaymentTxn(
        sender = account.address_from_private_key(private_key),
        sp = params,
        receiver = destino,
        amt = algos  # 1 ALGO = 1.000.000 microALGOs
        #,note=b"Hello Algorand"
    )

    # Assinar e enviar
    signed_txn = txn.sign(private_key)
    tx_id = client.send_transaction(signed_txn)
    print("ID da transação:", tx_id)

#cha = gerar_chaves()
#print(cha[0])  #chave privada
#print(cha[1])  #chave publica

