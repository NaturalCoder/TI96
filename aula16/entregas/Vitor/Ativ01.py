

try:
	num1 = float(input("Digite o primeiro número: "))
	num2 = float(input("Digite o segundo número: "))
	resultado = num1 / num2
except ZeroDivisionError:
	print("Não divide por zero seu animal")
except ValueError:
	print("Digita só numero, seu bosta")
else:
	print(f"O resultado da parada que você pediu : {resultado}")
finally:
    print("Fim do programa")
