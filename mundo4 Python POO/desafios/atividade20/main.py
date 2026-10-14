from classe import *

def main():
    a1 = DOC('prova', 25_000)
    p2 = PDF('documento', 250_000_000)

    abrir_arquivo(a1)
    abrir_arquivo(p2)
    
    print(p2.nome_completo)

if __name__=="__main__":
    main()