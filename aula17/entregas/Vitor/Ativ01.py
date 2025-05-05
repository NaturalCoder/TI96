class IdadeInvalida(Exception):
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalida("Idade inválida seu burro, tem que colocar número positivo")
    if idade >90:
        raise IdadeInvalida("tem que ser menor ou igual a 90 anos, você é o o que? o Matusalém?")


        

while True: 
    try:
        idade = int(input("Fala sua idade ai, vacilão: "))
        validar_idade(idade)
    except IdadeInvalida as e:
        print(e)
    except ValueError:
        print("Por favor, fala um número inteiro, seu bosta")
    else:
        print("Idade válida, Burro!")
        #print(f"Ai sim, molekote: {idade} anos.");
        break
    finally:
        print("Cabô, seu merda.")

    