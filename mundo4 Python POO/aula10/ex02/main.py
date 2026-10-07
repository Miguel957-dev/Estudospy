from classe import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    print(c1 == c2)
    
    c1 -= 100
    print(c1)

if __name__=="__main__":
    main()