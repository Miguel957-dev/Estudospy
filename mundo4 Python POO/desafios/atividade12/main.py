from personagens import *

def main():
    p1 = Guerreiro("MIGUEL", 2000)
    p2 = Mago("Kratos", 3000)

    p1.atacar(p2, 300)
    p2.curar()
if __name__== "__main__":
    main()

