"""
======================================================================
RESUMO DE PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
======================================================================
Paradigma que modela problemas reais usando "objetos" reutilizáveis.

--- CONCEITOS CENTRAIS ---
* Classe: O molde, a planta ou a receita (ex: a planta de uma casa).
* Objeto: A instância física criada a partir do molde (ex: a casa pronta).
======================================================================
"""

# --- OS 4 PILARES DA POO ---

# 1. ABSTRAÇÃO
# Esconder a complexidade e focar apenas no essencial.
# Ex: Você usa o volante do carro sem precisar entender a mecânica do motor.

# 2. ENCAPSULAMENTO
# Proteger os dados internos do objeto contra acessos diretos.
# Em Python: usamos '_' (protegido) ou '__' (privado) antes do nome da variável.

# 3. HERANÇA
# Criar classes novas que reaproveitam atributos e métodos de classes existentes.
# Ex: Classe 'Cachorro' herda as características gerais da classe 'Animal'.

# 4. POLIMORFISMO
# Métodos com o mesmo nome em classes diferentes que agem de formas distintas.
# Ex: O método 'falar()' faz o Cachorro latir e o Gato miar.


#declaração da clsse
class Gafanhoto:
    #Atributos
    def __init__(self):
        #Atributos de instacia
        self.nome = ""
        self.idade = 0
    
    #Métodos de instancia 
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de vida."


#Declaração de Objetos 

g1 = Gafanhoto()
g1.nome = 'Mguel'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

#obj = MinhaClasse() #Parentense é uma instanciação, chamando o metodos construtor (def__init__(self):)