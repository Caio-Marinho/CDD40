armazem = [0]*5
tamanho = len(armazem)
for i in range(tamanho):
    armazem[i] = int(input(f"Digite o {i+1}ª número: "))
for j in range(tamanho):
    print(f"{armazem[j]}",end='-->')
print("Ordem de inserção")
for inv in range(tamanho-1,-1,-1):
    print(f"{armazem[inv]}",end='-->')
print("Ordem inversar de inserção")