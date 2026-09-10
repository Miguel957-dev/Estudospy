""" Minimo de 16c e maximo de 30c
quando ligar ele fica em 24c e muda a temperatura de meio e meio graus celsius """
from rich import print

class Termostato:
    def __init__(self, temperatura = 24):
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura


    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura < 16:
            self.__temperatura = 16
            return
        elif temperatura > 30:
            self.__temperatura = 30
            return
        
        if temperatura % 0.5 != 0:
            raise ValueError (f"Temperatura {temperatura}°C é inválida")
    
        self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"
