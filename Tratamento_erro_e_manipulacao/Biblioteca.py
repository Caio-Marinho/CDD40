def cadastra(texto:str):
    with open('Registro.txt','a',encoding='UTF-8') as arq:
        arq.write(f"{texto}\n")

def mostrar():
    with open('Registro.txt','r',encoding='UTF-8') as arq2:
        leitura = arq2.read()
        yield leitura

