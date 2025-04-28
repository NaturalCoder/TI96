"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""
def divisao_segura():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if num2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")

# Chamada da função
divisao_segura()
