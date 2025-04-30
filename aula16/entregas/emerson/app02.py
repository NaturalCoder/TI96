"""
****  SEM USAR IA ****

Crie um gerenciador de contexto simplificado:
1. Tente abrir um arquivo
2. Trate FileNotFoundError
3. Use finally para garantir o fechamento do arquivo
"""

def ler_arquivo(pasta):
    try:
        arquivo = None
        arquivo = open(pasta, 'r')
    except FileExistsError:
        print(arquivo.read())
    finally:
        arquivo.close()
        print("Arquivo fechado com sucesso.")

ler_arquivo("dadosXX.txt") # Erro proposital de digitação (dados.txt)