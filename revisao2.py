rep = 1
while rep ==1:
    numero = int(input("Digite um número: "))
    if numero % 2 ==0:
        if numero > 0:
            print(f"{numero} é par e positivo")
        else:
            print(f"{numero} é par e negativo")
    else:
        if numero > 0:
            print(f"{numero} é impar e positivo")
        else:
            print(f"{numero} é impar e negativo")
    rep = int(input("Deseja repetir?\n"
                    "1 para sim\n"
                    "2 para não\n"
                    "Digite: "))