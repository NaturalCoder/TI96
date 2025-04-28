"""
****  SEM USAR IA ****

Crie um gerenciador de contexto simplificado:
1. Tente abrir um arquivo
2. Trate FileNotFoundError
3. Use finally para garantir o fechamento do arquivo
"""

def ler_arquivo(nome_arquivo):
    arquivo = None
    arquivo = open(nome_arquivo, 'r')
    print(arquivo.read())
    arquivo.close()
    print("Arquivo fechado com sucesso.")

ler_arquivo("dadosXX.txt") # Erro proposital de digitação (dados.txt)