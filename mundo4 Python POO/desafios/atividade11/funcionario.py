from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome = '', sal_bruto = 0, salario = 0, sal_min = 1612, inss = 00.75):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        analise = self.salario / self.sal_min
        return analise

class Horista(Funcionario):
    def __init__(self, nome , valor_hora = 0, hora_trab = 0):
        super().__init__(nome = nome)
        self.nome = nome
        self.valor_hora = valor_hora 
        self.hora_trab = hora_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.hora_trab
        self.salario = self.sal_bruto * self.inss


    def analisar_salario(self):
        analise = super().analisar_sal()

        conteudo = Panel(f"[white]O salário de [blue]{self.nome}[/blue] ([purple]FunciorarioHorista[/purple]) é de [green]R${self.salario} [/green] e corresponde a [yellow] {analise:.2f} salários mínimos.[/yellow] [/white]", title="Analise de salario", width = 50)
        print(conteudo)

class Mensalmente(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome = nome)
        self.nome = nome
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto * self.inss

    def analisar_salario(self):
        analise = super().analisar_sal()

        conteudo = Panel(f"[white]O salário de [blue]{self.nome}[/blue] ([purple]FunciorarioMensal[/purple]) é de [green]R${self.salario} [/green] e corresponde a [yellow] {analise:.2f} salários mínimos.[/yellow] [/white]", title="Analise de salario", width = 50)
        print(conteudo)

