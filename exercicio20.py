n1:int = int(input("Digite o 1º número: "))
n2:int = int(input("Digite o 2º número: "))
while n2 == 0 or n1==0 or (n1==0 and n2==0):
    if n1 ==0 and n2==0:
        print("Nenhuma das duas variaveis podem ser zero.")
        n1: int = int(input("Digite o 1º número: "))
        n2: int = int(input("Digite o 2º número: "))
    elif n1 ==0:
        print("A primeira variavel não pode ser zero")
        n2: int = int(input("Digite o 1º número: "))
    else:
        print("A segunda variavel não pode ser zero")
        n2:int = int(input("Digite o 2º número: "))
final:float = n1/n2
print(final)
