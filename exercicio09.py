time1:str = input("Digite o nome do 1º Time: ")
time1_gol:int = int(input(f"Quantidade de gols do {time1}: "))
time2:str = input("Digite o nome do 2º Time: ")
time2_gol:int = int(input(f"Quantidade de gols do {time2}: "))

if time1_gol == time2_gol:
    print(f"O jogo de {time1} X {time2} foi empatado")
else:
    if time1_gol > time2_gol:
        print(f"O jogo de {time1} X {time2} teve como vencedor o {time1} com {time1_gol} gols!!!")
    else:
        print(f"O jogo de {time1} X {time2} teve como vencedor o {time2} com {time2_gol} gols!!!")