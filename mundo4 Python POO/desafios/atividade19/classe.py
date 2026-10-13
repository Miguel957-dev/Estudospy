from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = '', salario:float = 0):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self._salario:
            raise ValueError("O novo salário não pode ser menor do que defindo antes!")
        else:
            self._salario = valor

    def __str__(self):
        return f'{self.nome} ganha {self._salario} no cargo {type(self).__name__} o bônus é de {self.calcular_bonus()}'

    @abstractmethod
    def calcular_bonus(self):
        pass

class Designer(Funcionario):
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self._salario * 0.08     
    

class Gerente(Funcionario):
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self._salario * 0.15  
   
class Desenvolvedor(Funcionario):
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self._salario * 0.1 
