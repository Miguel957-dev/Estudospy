
class Produto:
    def __init__(self, nome:str = '', preço:float = 0):
        self.nome = nome
        self.preço = preço
    
    
    def __str__(self):
        return f"{self.nome} R$ {self.preço:.2f}"
        

class Carrinho:
    def __init__(self, produto:list=None):
        self.produto = produto if produto else []

    @property
    def total(self):
        return  sum(p.preço for p in self.produto)

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produto + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produto + outro.produto)
        else:
            raise TypeError("Você tentou adicionar algo inválido.")

    def __str__(self):
        linha = '\n' + '-'*30
        itens = ', ' .join(str(p) for p in self.produto) ,'\n'
        return f'{itens} Total: {self.total}{linha}'