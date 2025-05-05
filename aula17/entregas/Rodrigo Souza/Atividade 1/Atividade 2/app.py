class SenhaFracaError(Exception):
    pass

def validarsenha(senha):
    if len(senha) < 8:
        raise SenhaFracaError("Senha muito curta.")

try:
    validarsenha("minhasenha")
    print("Senha ok.")
except SenhaFracaError as e:
    print(e)