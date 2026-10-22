from classe import *

def main():

    a = [Aluno('Miguel', 'Edificações', "terceiro"),
         Aluno('Hérica', 'Biotecnologia', 'terceiro')]

    b = [Usuario("miguel", 'miguel.queiroz@gmail.com'),
         Usuario("Ester", 'ester.lopes@gmail.com')]
    exportar_dados(XML(), a)
    exportar_dados(JSON(), b )

if __name__=="__main__":
    main()