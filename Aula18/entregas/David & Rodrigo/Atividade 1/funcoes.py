def validar_cpf(cpf):
    """
    Valida um CPF verificando seu formato e dígitos verificadores.
    
    Args:
        cpf: String contendo o CPF (com ou sem pontuação)
    
    Returns:
        bool: True se o CPF é válido, False caso contrário
    """
    
  
    cpf = ''.join(filter(str.isdigit, cpf))
    
   
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
   
    def calcular_digito(cpf, pesos):
        """
        Calcula o dígito verificador com base nos primeiros 9 ou 10 números do CPF.
        
        Args:
            cpf: Lista com os números do CPF.
            pesos: Lista de pesos usados no cálculo do dígito.
        
        Returns:
            int: O dígito verificador calculado.
        """
        soma = sum(int(cpf[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    
    digito1 = calcular_digito(cpf, list(range(10, 1, -1)))
    
    digito2 = calcular_digito(cpf, list(range(11, 1, -1)))
    
    
    if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
        return False
    
    return True
