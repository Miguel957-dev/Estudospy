#O que fazer quando tiver mais de duas opções para um problema ao inves de duas. Chamados de Condições Aninhadas 

if 3:
    4
elif 5: #Funciona para disponiblizar mais uma opção ao programa. Podendo ser usado varios elif, e não é obrigatorio o else mas apenas o if, o elif é sempre usado a parti do momento que se aumenta uma possibilidade ao programa 
    4
else:
    6

nome = str(input('Digite seu nome: '))
if nome == 'Miguel':
    print('Que nome bonito o seu!')
elif nome == 'Pedro' or nome =='Maria' or nome == 'João':
    print('Nome muito popular aqui no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'. format(nome))