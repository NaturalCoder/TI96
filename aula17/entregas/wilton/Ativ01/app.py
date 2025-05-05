"""
********

Crie uma exceção personalizada:
1. Crie a classe IdadeInvalida herdando de Exception
2. Faça uma função que valide idades
3. Lance a exceção personalizada quando necessário
"""

class IdadeInvalidade(Exception):
    
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalidade("Idade negativa não permitida!")
    print(f"Idade válida : {idade} anos")

def main ():
    try:
        idade = int(input("Digita sua idade: "))
        validar_idade(idade)

    except ValueError:
        print("Erro precisa digitar um numero inteiro: ")
    except IdadeInvalidade as e:
        print(f"Erro idade Invalidade: {e}")
    finally:
        print ("Programa finalizado")

if __name__ == '__main__':
    main()
    