repetir = 1
while repetir == 1:
    nota1 = float(input("Digite a 1º Nota: "))
    while 0>nota1 or nota1>10:
        nota1 = float(input("Digite a 1º Nota como uma nota valida sendo maior igual a 0 e menor ou igual a 10: "))
    nota2 = float(input("Digite a 2º Nota: "))
    while 0>nota2 or nota2>10:
        nota2 = float(input("Digite a 2º Nota como uma nota valida sendo maior igual a 0 e menor ou igual a 10: "))
    media = (nota1+nota2)/2
    print(f"A média foi: {media} pontos")
    repetir = int(input("Deseja repetir novamente?\n1 para sim\n2 para não\nDigite: "))