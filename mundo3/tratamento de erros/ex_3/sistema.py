from lib.interface import *
from lib.arquivo import *
from time import sleep

aqr = 'mundo3/tratamento de erros/ex_3/cursoemvideo.txt'

if not arquivoexite(aqr):
    criArquivo(aqr)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar pessoas', 'Sair do sitema'])
    if resposta == 1:
        lerarquivo(aqr)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaint('Idade: ')
        cadastrar(aqr, nome, idade)
    elif resposta ==3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('ERROR! Digite uma opção valida')
    sleep(2)
