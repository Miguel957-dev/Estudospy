from rich import print
from poligno import *


def main():
    p1 = Quadrado(5)
    p1.perimetro()
    p1.area()

    c1 = Circulo(3)
    c1.perimetro()
    c1.area()

if __name__ == "__main__":  
    main()