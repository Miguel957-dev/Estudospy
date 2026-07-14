from rich import print
from rich import inspect
class Funcionario:
    #Atributo de Classe 
    empresa = "Curso em Video"

    def __init__(self, nome = "", setor = "", cargo = ""):
        #Atributo de instancia 
        self.nome = nome
        self.setor = setor
        self.cargo = cargo



    def apresentar(self) -> str:
        return f":handshake: Olá eu sou [blue]{self.nome}[/blue], trabalho no setor {self.setor} no cargo de {self.cargo} da empresa {Funcionario.empresa}"


p1= Funcionario('Miguel', 'Desenvolvimento', 'dev senior')
#inspect(p1, methods=True)
print(p1.apresentar())   

p2= Funcionario('João', 'Adiministrativo', 'Contador')
print(p2.apresentar())