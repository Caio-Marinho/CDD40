class Pessoa:

    def __init__(self,nome,idade):
        self.__idade = idade
        self.__nome = nome

    def idade(self):
        return self.__idade

    def anivesario(self):
        self.__idade = self.idade() + 1

    def nome(self):
        return self.__nome

    def falar(self):
        return f"{self.nome()} fala português!"

class Espanhol(Pessoa):
    def falar(self):
        return f"{self.nome()} fala espanhol!"