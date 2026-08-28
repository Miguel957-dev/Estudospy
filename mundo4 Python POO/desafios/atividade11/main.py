from funcionario import *

def main():

    T1 = Horista("Miguel", 12, 400)
    T1.calc_sal()
    T1.analisar_salario()

    F2 = Mensalmente("Luma", 1500)
    F2.calc_sal()
    F2.analisar_salario()

if __name__ == "__main__":
    main()