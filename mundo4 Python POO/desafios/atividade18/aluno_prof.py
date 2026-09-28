from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC): #SUPERCLASSE
    def __init__(self, nome:str='', nascimento:int=0):
       self._nome = nome
       self._nascimento = None
       self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nacimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError('Você não pode mudar a idade. Mude o nascimento. ')
    

class Aluno(Pessoa):#CLASSE

    curso_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome:str, nascimento:int, curso:str, ):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        if curso in Aluno.curso_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não esta na lista")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()

        if  3 <= len(curso) <= 10:
            Aluno.curso_oficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} está fora do padrão para Cursos!")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade =  especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no {self.nivel}.')
        pass

