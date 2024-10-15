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

    def comer(self):
        print(f"O Gato {self.nome} foi comer")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"O cachorro {self.nome} latiu")

    def comer(self):
        print(f"O Cachorro {self.nome} foi comer")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A vaca {self.nome} mugiu")

    def comer(self):
        print(f"A Vaca {self.nome} foi comer")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def grunir(self):
        print(f"O coelho {self.nome} Gruniu")

    def comer(self):
        print(f"O Coelho {self.nome} foi comer")


class Atleta:
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecendo = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def aposetar(self):
        if not self.aposentado:
            self.aposentado = True
            print(f"O atleta {self.nome} foi aposentado")
        else:
            print(f"O atleta {self.nome} já foi aposentado")


    def aquecer(self):
        if not self.aposentado:
            if not self.aquecendo:
                self.aquecendo = True
                print(f"{self.nome} está aquecendo")
            else:
                print(f"{self.nome} já está aquecendo")
        else:
            print(f"{self.nome} não pode aquecer pois está aposentado")

class Corredor(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)

    def correr(self):
        if self.aquecendo:
            if self.nadando:
                print(f"{self.nome} não pode correr, pois está nadando")
            elif self.pedalando:
                print("f{self.nome} não pode correr, pois está pedalando")
            else:
                if not self.correndo:
                    self.correndo = True
                    print(f"{self.nome} foi correr")
                else:
                    print(f"{self.nome} já está correndo")
        else:
            print(f"{self.nome} não pode correr pois não se aqueceu")

    def pararCorrer(self):
        if self.aquecendo:
            if self.correndo:
                print(f"{self.nome} parou de correr")
                self.correndo = False
            else:
                print(f"{self.nome} já parou de correr")
        else:
            print(f"{self.nome} não chegou a nem correr pois não aqueceu")

class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)


    def nadar(self):
        if self.aquecendo:
            if self.correndo:
                print(f"{self.nome} não pode nadar, pois está correndo")
            elif self.pedalando:
                print(f"{self.nome} não pode nadar, pois está pedalando")
            else:
                if not self.nadando:
                    self.nadando = True
                    print(f"{self.nome} foi nadar")
                else:
                    print(f"{self.nome} já está nadando")
        else:
            print(f"{self.nome} não pode nadar pois não se aqueceu")

    def pararNadar(self):
        if self.aquecendo:
            if self.nadando:
                print(f"{self.nome} parou de nadar")
                self.nadando = False
            else:
                print(f"{self.nome} já parou de nadar")
        else:
            print(f"{self.nome} não chegou a nem nadar pois não aqueceu")

class Ciclita(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)


    def pedalar(self):
        if self.aquecendo:
            if self.nadando:
                print(f"{self.nome} não pode pedalar, pois está nadando")
            elif self.correndo:
                print(f"{self.nome} não pode pedalar, pois está correndo")
            else:
                if not self.pedalando:
                    self.pedalando = True
                    print(f"{self.nome} foi pedalar")
                else:
                    print(f"{self.nome} já está padalar")
        else:
            print(f"{self.nome} não pode padalar pois não se aqueceu")

    def pararPedalar(self):
        if self.aquecendo:
            if self.pedalando:
                print(f"{self.nome} parou de pedalar")
                self.pedalando = False
            else:
                print(f"{self.nome} já parou de pedalar")
        else:
            print(f"{self.nome} não chegou a nem pedalar pois não aqueceu")

class TriAtleta(Corredor,Nadador,Ciclita):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)