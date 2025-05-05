"""
****  SEM USAR IA ****

Crie um gerenciador de contexto simplificado:
1. Tente abrir um arquivo
2. Trate FileNotFoundError
3. Use finally para garantir o fechamento do arquivo
"""

def ler_arquivo(nome_arquivo):
    try:
        # 1. Tentar abrir o arquivo
        arquivo = open(nome_arquivo, 'r')
        print(arquivo.read())
    
    except FileNotFoundError:
        # 2. Tratar erro de arquivo não encontrado
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    finally:
        # 3. Garantir que o arquivo seja fechado
        if arquivo:
            arquivo.close()
            print("Arquivo fechado com sucesso.")
        else:
            print("Nenhum arquivo foi aberto.")

# Teste com erro proposital no nome do arquivo
ler_arquivo("dadosxx.txt")
