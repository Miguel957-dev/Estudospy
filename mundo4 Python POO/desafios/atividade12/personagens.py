from abc import ABC, abstractmethod
from random import *

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = [] 

    def atacar(self, alvo, força = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f"{self.nome} atacou {alvo.nome} com um {golpe}.")
            alvo.receber_dano(força)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')
        


    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida = self.vida - fator
        print(f"{self.nome} atacou com a força de {fator}")
        if self.vida < 0:
            self.vida = 0

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratorio"]


    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"{self.nome} usou faixa para se curar, e ganhou mais {fator} de vida")

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]


    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"{self.nome} usou magia para se curar, e ganhou mais {fator} de vida")