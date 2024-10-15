class Pessoa:
    def __init__(self,nome:str,peso:float,idade:int,comendo:bool=False,dormindo:bool=False,andando:bool=False):
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

class Animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O gato {self.nome} foi miar")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"O cachorro {self.nome} latiu")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A vaca {self.nome} mugiu")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def grunir(self):
        print(f"O coelho {self.nome} Gruniu")