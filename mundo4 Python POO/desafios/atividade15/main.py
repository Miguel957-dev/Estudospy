from criptografia import *

def main():
    c = Credencial()
    c.senha = 'Miguel'
    print(c.senha)
    c.validar('Miguel')

if __name__ == "__main__":
    main()