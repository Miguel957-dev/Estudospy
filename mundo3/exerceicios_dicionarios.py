#  Exercicios de Dicionarios

# Primeiro exercicio 

'''aluno_info = {}
aluno_info['Nome'] = input('Qual é o nome do aluno ? ')
aluno_info['Media'] = int(input(f'Qual é a media do aluno {aluno_info["Nome"]}? '))
if aluno_info['Media'] < 7:
    aluno_info['Situação'] = 'Reprovado'
else:
    aluno_info['Situação'] = 'Aprovado'
for k, v in aluno_info.items():
    print(f'{k} é igual a {v}')
'''

# Segundo exercicio 

'''from random import randint
import time


jogadores = {'Jogador1':randint(1, 6), 
             'Jogador2':randint(1, 6),
             'Jogador3':randint(1, 6),
             'Jogador4':randint(1,6)
             }
print('Valores sorteados!')
for k, v in jogadores.items():
    print(f'O jogador {k} sorteou {v}.')
    time.sleep(1)
dic_oderm_decres = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

print('===========RANKIG===========')
for i , v in enumerate(dic_oderm_decres):
    print(f'{i + 1}º Lugar foi o {v[0]} que tirou {v[1]} ')
    time.sleep(1)
'''


# Terceiro exercicio 

'''from datetime import datetime

ano_atual = datetime.today().year 

informaçoes = {}


informaçoes['Nome'] = input('Digite seu nome: ')
ano_nasc = int(input('Digite o ano de nascimento: '))
informaçoes['Carteira'] = int(input('Carteira de trabalho (Digite 0 se não tem)'))
informaçoes['Idade'] = ano_atual - ano_nasc 
if informaçoes['Carteira'] == 0:
    for k, v in informaçoes.items():
        print(f'{k}: {v}')
else:
    informaçoes['Contratação'] = int(input('Qual o ano da contratação: '))
    informaçoes['Sálario'] = input('Sálario: R$')
    temp_trabalho = ano_atual - informaçoes['Contratação'] 
    faltam =  35 - temp_trabalho
    informaçoes['Aposentadoria'] = faltam + informaçoes['Idade']
    for k, v in informaçoes.items():
        print(f'{k} é igual á {v}.')
'''

# Quarto exercicio 

'''jogador = {}
gols_lista = []
tot_gols = 0

jogador['Nome'] = input('Qual é o nome do jogador? ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
if partidas > 0:
    for c in range(0, partidas):
        gol = int(input(f'  Quantos gols na partida {c}? '))
        gols_lista.append(gol)
for c, v in enumerate(gols_lista):
    tot_gols += v
jogador['total'] = tot_gols
jogador['gol'] = gols_lista

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas}.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {gols_lista[c]}')
print(f'Foi um total de {tot_gols}.')
'''

# Quarto exercicio 

'''quan_pessoas = soma_idade = media = 0
dict_pessoas = {}
galera = []
mulheres = []
while True:
    dict_pessoas.clear()
    dict_pessoas['nome'] = input('Nome: ')
    while True:
        dict_pessoas['sexo'] = input('Sexo [M/F]').upper() .strip()
        if dict_pessoas['sexo'] in ['M', 'F']:
            break
        else:
            print('Por favor so digite M ou F.') 
    if dict_pessoas['sexo'] in 'F':
        mulheres.append(dict_pessoas['nome'[:]])
    dict_pessoas['idade'] = int(input('Idade: '))
    soma_idade += dict_pessoas['idade']
    galera.append(dict_pessoas.copy())
    while True:
        s_n = input('Quer continuar[S/N]').upper() .strip()
        if s_n in ['S', 'N']:
            break
        else:
            print('Por favor digite um valor valido. ')
    quan_pessoas += 1
    if s_n in ['N']:
        break
media = soma_idade / quan_pessoas
print(f'A) Ao todo temos {quan_pessoas} pessoas cadastradas.')
print(f'B) A média da idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista das pessoas que estão acima da média.')
for d in galera:
    if d['idade'] > media:
        print(f'    Nome = {d["nome"]}; Sexo = {d["sexo"]}; Idade = {d["idade"]}')
print('<<ENCERRADO>>')'''

# Quinto exercicio

lista_jogador = []
jogador = {}
gols_lista = []
tot_gols = 0
cont = []

while True:
    gols_lista.clear()
    jogador.clear()
    jogador['Nome'] = input('Qual é o nome do jogador? ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
    if partidas > 0:
        for c in range(0, partidas):
            jogador['gol'] = int(input(f'  Quantos gols na partida {c}? '))
            gols_lista.append(jogador['gol'])
    for c, v in enumerate(gols_lista):
        tot_gols += v
    jogador['total'] = tot_gols
    jogador['gol'] = gols_lista[:]
    lista_jogador.append(jogador.copy())
    while True:
        s_n = input('Quer continuar [S/N] ?').upper() .strip()
        if s_n not in ['S', 'N']:
            print('Valor invalído por favor tente novamente.')
        if s_n  in ['S', 'N']:
            break
    if s_n in 'N':
        break
print('-='*30)
print(f"{'cod':<3} {'Nome':<15} {'Gols':>20} {'Total':>5}")
print('-'*30)
for c, d in enumerate(lista_jogador):
    print(f'{c:<3} {d["Nome"]:<15} {str(d["gol"]):>20} {d["total"]:>5}')
    cont.append(c)
print('-='*30)
while True: 
    qual_jog = int(input('Qual dados de qual jogador?  [Digite: 999 para cancelar.]'))
    if qual_jog == 999:
        break
    elif qual_jog not in enumerate(lista_jogador):
        print('Não temos esse joagdor no time.')
    print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogador[qual_jog]["Nome"]}')
    for c, gols_no_jogo in enumerate(lista_jogador[qual_jog]["gol"]):
        print(f'    No jogo {c + 1} fez {gols_no_jogo} gols')

        





