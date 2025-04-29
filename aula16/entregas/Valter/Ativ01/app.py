"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""
#crie um programa em python que peça dois numeros ao usuario e divida o primeiro pelo segundo, trate divisão por zero por mensagem clara e trate entrada inválidas com mesagem específicas

def dividirNumeros():

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2

    except ZeroDivisionError: 
        print("Erro: Não é divisível por zero")   
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.") 
    else: 
        print(f"O resultado da divisão é: (resultado)")





dividirNumeros()