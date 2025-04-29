def ler_arquivo(nome_arquivo):
    arquivo = None
    try:
        arquivo = open(nome_arquivo, 'r')
        print(arquivo.read())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado com sucesso.")

# Teste com erro proposital
ler_arquivo("dadosXX.txt")
