from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar pessoas', 'Sair do sitema'])
    if resposta == 1:
        cabeçalho('Opção1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta ==3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('ERROR! Digite uma opção valida')
    sleep(2)
