from diario import *

def main():
    d1 = Diario()
    d1.escrever("Minha namorada é linda")
    d1.escrever("Eu amo muito ela")
    try:
        d1.ler("linda")
    except Exception as e:
        print(f'[red]ERRO: {e}')


if __name__ == "__main__":
    main()
