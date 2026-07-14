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
    
    
    def __str__(self): #Mostrar os dados de uma maneira mais amigavel
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de vida."
    
    def __getstate__(self):
        return f"Estado: nome {self.nome}; idade = {self.idade}"
    

#Declaração de Objetos 

g1 = Gafanhoto('Miguel', 17)
g1.aniversario()
print(g1)

print(g1.__doc__)

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3.__dict__)#Vai trabalhar com as informações em forma de dicionario sendo atributos
print(g2.__getstate__())#Esse é um metodo, podendo reescrever os str


#obj = MinhaClasse() #Parentense é uma instanciação, chamando o metodos construtor (def__init__(self):)

print(g1.__class__)#Mostra qual classe o objeto pertence
