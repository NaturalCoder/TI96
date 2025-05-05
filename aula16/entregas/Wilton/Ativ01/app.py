"""
****  SEM USAR IA ****

Crie um programa que:
1. Peça dois números ao usuário
2. Divida o primeiro pelo segundo
3. Trate divisão por zero com mensagem clara
4. Trate entradas inválidas com mensagem específica
"""
try:
    a = float(input('PRIMEIRO NUMERO --> '))
    b = float(input('SEGUNDO NUMERO --> '))
    z = a / b
    print("O RESULTADO é ", z)
    print("FINAL DO EXERCÍCIO1")
except ZeroDivisionError:
    print("NÃO ACEITA A DIVISÃO POR ZERO")
except ValueError:
    print("NÃO ACEITA CARACTERES OU LETRAS ")
finally:
    print("FINAL DO EXERCÍCIO2")