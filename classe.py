class Pessoa:
    def __init__(self,nome:str,peso:float,idade:int,comendo=False,dormindo=False,andando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.dormindo = dormindo
        self.comendo = comendo
        self.andando = andando

    def andar(self):
        if self.comendo:
            print(f"{self.nome} não pode ir andar pois está comendo")
        elif self.dormindo:
            print(f"{self.nome} não pode ir andar pois está dormindo")
        else:
            if not self.andando:
                self.andando = True
                print(f"{self.nome} foi andar")
            else:
                print(f"{self.nome}  já está andando")

    def parou(self):
        if self.andando:
            self.andando = False
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não está andando")

    def comer(self):
        if self.andando:
            print(f"{self.nome} não pode ir comer pois está andando")
        elif self.dormindo:
            print(f"{self.nome} não pode ir comer pois está dormindo")
        else:
            if not self.comendo:
                self.comendo = True
                print(f"{self.nome} foi comer")
            else:
                print(f"{self.nome} já está comendo")

    def terminou(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} terminou de comer")
        else:
            print(f"{self.nome} não está comendo")

    def dormir(self):
        if self.andando:
            print(f"{self.nome} não pode ir dormir pois está andando")
        elif self.comendo:
            print(f"{self.nome} não pode ir dormir pois está comendo")
        else:
            if not self.dormindo:
                self.dormindo = True
                print(f"{self.nome} foi domir")
            else:
                print(f"{self.nome} já está dormindo")

    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print(f'{self.nome} acordou')
        else:
            print(f'{self.nome} já está acordado')
