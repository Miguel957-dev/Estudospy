#ABSTRAÇÃO simplificar as coisas e deixar a redundancia 
#ENCAPSULAMENTO Protejer as partes importantes do codigo 
#HERANÇA hierarquia dos dados 
#POLIMORFISMO atividade de mesmo nome de formas diferentes 
 
# como a aula é de herança vamos começar com o conceito de herança
#Herança é um relacionamento entre itens gerais(ancestrais) e tipo mais especificos (descendentes) desses itens, que herdam atributos e metodos dos niveis superiores
# VANTAENS : Reutilização de codigos, Organização hierárquica, facilita manuntenção, extentensibilidade, Suporte a polimorfismo, 
#PRÁTICAA

class Pessoa: #SUPERCLASSE
    def __init__(self, nome='', idade=0):
       self.nome = nome
       self.idade = idade 

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):#CLASSE
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = ''
        self.turma = ''
    

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade =  ''
        self.nivel = ''


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = ''
        self.setor = ''

        def bater_ponto(self):
            pass


