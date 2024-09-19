valor = int(input("Digite um valor que fará um intervalo de 1 até esse numero: "))

for i in range(1,valor+1):
    if i%2==1:
        print(f"O número {i} é impar!!")