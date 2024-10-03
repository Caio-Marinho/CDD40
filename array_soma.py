n = int(input("Informe o tamanho o vetor: "))
v1 = [0]*n
v2 = [0]*n
v3 = [0]*n
for i in range(n):
    v1[i] = int(input(f"Digite o {i}º número para o vetor 1: "))
for j in range(n):
    v2[j] = int(input(f"Digite o {j}º número para o vetor 2: "))

for x in range(n):
    v3[x] = v1[x] + v2[x]
print(v3)
