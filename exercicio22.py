confirma = 1
contagem = 0
while confirma ==1 and contagem<=3:
    somaNegativo = 0
    for i in range(1,11):
        numero = int(input(f"Informe o {i}º número: "))
        if numero < 0 :
            somaNegativo+=1
    print(f"foram apresentados um toda de {somaNegativo} números negativos")
    confirma = int(input("\nDeseja digitar outro numero...\n1 - SIM\n2 - NÃO\n"))
    contagem+=1