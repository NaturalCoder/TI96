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
        n1 = float (input("Digite um numero "))
        n2 = float (input("Digite um numero "))

        resultado = n1 / n2
    except ValueError:

        print(f"Erro {ERROUUU}.")

    else:
        print(f"Resultado : {resultado}")


    

divisao_segura()



    













