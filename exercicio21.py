confirma = 1
while confirma ==1 :
    numero = int(input("Digite um numero: "))
    while numero <= 0:
        numero = int(input("Digite um numero maior que zero: "))
    for i in range(1,numero+1):
        print(i, end= ' ')
    confirma = int(input("\nDeseja digitar outro numero...\n1 - SIM\n2 - NÃO\n"))
