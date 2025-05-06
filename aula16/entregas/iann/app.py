try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
else:
    print(f"O resultado da divisão é: {resultado}")
finally:
    print("Operação finalizada.")