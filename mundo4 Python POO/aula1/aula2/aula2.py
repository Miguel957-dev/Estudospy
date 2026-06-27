#declaração da clsse
class Gafanhoto:
    """Essa classe cia um Gafanhoto que é uma pessoa com nome e idade"""
    #Atributos
    def __init__(self, nome = "Não informado", idade = 0):
        #Atributos de instacia
        self.nome = nome
        self.idade = idade
    
    #Métodos de instancia 
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de vida."

    def __str__(self):
        return "Vou te mostrar uma coisa. "
#Declaração de Objetos 

g1 = Gafanhoto('Miguel', 17)
g1.aniversario()
print(g1.mensagem())

print(g1.__doc__)

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

#obj = MinhaClasse() #Parentense é uma instanciação, chamando o metodos construtor (def__init__(self):)