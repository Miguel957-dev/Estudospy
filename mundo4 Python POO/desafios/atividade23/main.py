from classe import *

def main():
    p1 = Produto('RTX 5090TI', 2000)
    p2 = Produto('I9 9000', 3000)
    
    c1 = Carrinho()
    c1 =  c1 + p1 + p2    
    print(c1)
if __name__=="__main__":
    main()