from rich import print
from rich.panel import Panel
from rich.align import Align  # Importante importar o Align

class Produto:

    def __init__(self, nome = '', valor = None):
        
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        nome_centralizado = f"[center][white]{self.nome}[/white][/center]"
        linha_divisoria = "[white]" + "-" * 46 + "[/white]"
        preco_formatado = f"R${self.valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        valor_formatado = f"[white]{preco_formatado:.^46}[/white]"
        conteudo = f"{nome_centralizado}\n{linha_divisoria}\n{valor_formatado}"
        Align.center(conteudo)
        caixa = Panel(conteudo, title="Produto", style="white", expand=False) 
        print(caixa)
        


p1 = Produto('Notebook', 3500)
p1.etiqueta()