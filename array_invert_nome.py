nomes = ['']*5
tamanho = len(nomes)
for i in range(tamanho):
    nomes[i] = input("Digite o nome: ")
for nome in nomes:
    print(nome)
print()
for inverte in nomes[::-1]:
    print(inverte)
