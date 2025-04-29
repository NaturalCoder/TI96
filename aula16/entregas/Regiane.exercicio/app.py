"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""
def divisao_segura():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    try:
        
        resultado = numero1 / numero2
    except ValueError as e:
           
        print(f"Erro: {e}.")

    else:
        print(f"Resultado: {resultado}")


divisao_segura()

