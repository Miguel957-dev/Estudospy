def linha(tam = 42):
    return'-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interropida pelo usuario')
            break
        else:
            return n 
        

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc