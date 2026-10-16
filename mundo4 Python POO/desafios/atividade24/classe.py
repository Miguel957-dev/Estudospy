from abc import ABC, abstractmethod
import re 

class Validador(ABC):

    @abstractmethod
    def validar(self, valor:str)-> bool:
        pass

class Usuario(Validador):
    def validar(self, valor)-> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            False

class Email(Validador):
    def validar(self, valor)-> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            False

class Senha(Validador):
    def validar(self, valor)-> bool:
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            False 
def validar_dados(Validador, valor:str):
    resultado = Validador.validar(valor)
    print(f"Valor: {valor} é válido? {'SIM' if resultado else 'NÃO'}")