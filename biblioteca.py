def imprimir_nome(nome):
    return f"Nome:{nome}"

def imprimir_numero(n):
    for i in range(1,n+1,1):
        print(i,end=' ')

def somar(*lista):
    soma = 0
    for i in lista:
        soma+=i
    print(f"A soma de {'+'.join(map(str,lista))} é {soma}")

def contagem_letra(*textos):
    cont = 0
    for texto in textos:
        for letra in texto:
            if letra != ' ':
                cont+=1
        print(f"O texto '{texto}' tem {cont} letras")
        cont = 0
    for texto in textos:
        for invertido in texto[::-1]:
            print(invertido,end='')
        print()

def tira_repeticao(lista:list[int]):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    print(nova_lista)

def primo(n):
    cont = 0
    if n ==1:
        print("Não é Primo")
    for i in range(2,(n//2)+1):
        if n%i==0:
            cont+=1
    if cont==0:
        print("É Primo")
    else:
        print("Não é Primo")