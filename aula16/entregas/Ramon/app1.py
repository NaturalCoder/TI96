def dividir_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos.")

if __name__ == "__main__":
    dividir_numeros()
