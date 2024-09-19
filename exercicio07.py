numero1:float = float(input("Digite o 1º Valor: "))
numero2:float = float(input("Digite o 2º Valor: "))

if numero1 == numero2:
    print("Ambos são iguais")
    print(f"{numero1}=={numero2}")
else:
    if numero1 > numero2:
        print(f"O numero1: {numero1} é maior que numero2: {numero2}")
        print(f"{numero2}<{numero1}")
    else:
        print(f"O numero2: {numero2} é maior que numer1: {numero1}")
        print(f"{numero1}<{numero2}")
