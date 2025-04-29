"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""

def divisao_segura():
    while True:
        try:
            # 1. Pedir dois números ao usuário
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            
            # 2. Dividir o primeiro pelo segundo
            resultado = numero1 / numero2
            
            # Se a divisão for bem-sucedida, mostramos o resultado e saímos do loop
            print(f"O resultado da divisão é: {resultado}")
            break
        
        except ZeroDivisionError:
            # 3. Tratar divisão por zero
            print("Erro: Não é possível dividir por zero.")
        
        except ValueError:
            # 4. Tratar entradas inválidas
            print("Erro: Por favor, insira apenas números válidos.")

# Chamando a função
divisao_segura()
