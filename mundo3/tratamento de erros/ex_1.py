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
        

num = leiaint('Digite um valor inteiro: ')
print(f'O valor digitado foi {num}')