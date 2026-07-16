from rich import print
from rich.panel import Panel
#Consumo por pessoa 400g
# Preço :R$82,40/kg

class Churrasco:
    preço = 82.4
    consumo_pessoa = 0.4 

    def __init__(self, nome = '', pessoas = 0):

        self.nome = nome
        self.pessoas = pessoas
        
    def calcular_quantidade_carne(self):
        return self.pessoas * self.consumo_pessoa
    
    def calcular_custo_total(self):
        self.valor = self.calcular_quantidade_carne() * self.preço
        return self.valor     

    def valor_por_pessoa(self):
        self.valorpor_pessoa = self.valor / self.pessoas
        return self.valorpor_pessoa
    
    def analisar(self):
   
        analise = f"[white]Analisando [green]{self.nome}[/green] com [blue]{self.pessoas}[/blue] convidados.[/white]"
        descriçao = f"[white]Cada pessoa comerá 0.4 kg e cada Kg custa R$82.40 [/white]"
        compra = f"Recomendo comprar {self.calcular_quantidade_carne():,.2f} Kg".replace(",", "X").replace(".", ",").replace("X", ".")
        custo = f"[white]O custo total será R${self.calcular_custo_total():,.2f}[/white]"
        custo_pessoa = f"[white]O custo total será R${self.valor_por_pessoa():,.2f}[/white]"

        conteudo = f"{analise}\n{descriçao}\n{compra}\n{custo}\n{custo_pessoa}"
        
        caixa = Panel(conteudo, title="Produto", style="white", expand=False) 
        print(caixa)

chu1 = Churrasco('Churrasco igreja', 10)
chu1.analisar()