"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""


prompt = "Digite um número: "

def divisao_segura():
    try:
        n1 = float(input(prompt))
        n2 = float(input(prompt))
        if n2 == 0:
            print("Não é possível dividir por zero.")
        if n1 == 0:
            print("Não é possível dividir por zero.")
        else:
            print("Resultado:", n1 / n2)
    except ValueError:
        print("Por favor, digite apenas números.")
    except Exception as erro:
        print("Ocorreu um erro:", erro)

divisao_segura()




