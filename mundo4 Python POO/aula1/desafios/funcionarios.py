""" from rich import print as rprint """
class Funcionario:
    def __init__(self, nome = "", setor = "", cargo = ""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá eu sou o funcionario {self.nome}, trabalho no setor {self.setor} no cargo de {self.cargo}"

p1= Funcionario('Miguel', 'Desenvolvimento', 'dev senior')
print(p1.apresentar())