from aluno_prof import *

def main():
    a = Aluno('MIguel', 2009, "ADM")
    a.add_curso("Moda")
    print(a.curso_oficiais)
    print(a.__dict__)

if __name__=="__main__":
    main()

#VERIFICAÇÃO DE REPETIÇÃO DE CURSOS 
