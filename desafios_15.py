'''s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n 
    cont += 1
#print('A soma  vale {}.'. format(s))
print(f'A soma dos {cont} valores é {s}!')

while True:
    N = int(input('Digite um numero:  '))
    if N < 0:
        break
    print(f'A tabuada do {N} de 1 até 10 é')
    print(f"{N} x 2 = {N*1}")
    print(f"{N} x 2 = {N*2}")
    print(f"{N} x 3 = {N*3}")
    print(f"{N} x 4 = {N*4}")
    print(f"{N} x 5 = {N*5}")
    print(f"{N} x 6 = {N*6}")
    print(f"{N} x 7 = {N*7}")
    print(f"{N} x 8 = {N*8}")
    print(f"{N} x 9 = {N*9}")
    print(f"{N} x 10 = {N*10}")
print('Programa da tabuada encerrado. Volte sempre!') 


from random import randint
quantas_vitorias = 0
while True:
    print(20*'=-')
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    print(20*'=-')
    num_jogador = int(input('Diga um valor: '))
    par_ou_impar = str(input('Par ou impar[P/I]')).strip() .upper()
    if par_ou_impar not in ('P', 'I'):
        while par_ou_impar not in ('P', 'I'):
            print('Resposta invalida, por favor digite novamente.')
            par_ou_impar = str(input('Par ou impar[P/I]')).strip() .upper()
    num_computador = randint(1, 10)
    num_verificaçao = num_computador + num_jogador
    if num_verificaçao % 2 == 0:
        pi_resultado = 'PAR'
    else:
        pi_resultado = 'IMPAR'
    print(f'Você jogou {num_jogador} e o computador {num_computador}. Total de {num_verificaçao} deu {pi_resultado}!')
    if num_verificaçao % 2 == 0 and par_ou_impar == 'P':
        print('PARABÉNS, VOCÊ GANHOU')
        quantas_vitorias += 1
    elif num_verificaçao % 2 == 0 and par_ou_impar == 'I':
        print('Voce perdeu')
        print(f'GAMER OVER! Total de {quantas_vitorias} vitórias!')
        break
    if num_verificaçao % 2 != 0 and par_ou_impar == 'I':
        print('Parabéns! Você GANHOU!')
        quantas_vitorias += 1 
    elif num_verificaçao % 2 != 0 and par_ou_impar == 'P':
        print('Você perdeu!')
        print(f'GAMER OVER! Total de {quantas_vitorias} vitórias!')
        break
print('Acabou!')

mulheres_menor_20 = 0
homens = 0
maioridade = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')). strip() . upper()
        if sexo in ('M' , 'F'):
            break
    if sexo == 'M':
        homens += 1
    while True:
        continuar = str(input('Quer continuar ? [S/N]')). strip() . upper()
        if continuar in ('S' , 'N'):
            break
    if idade < 20 and sexo == 'F':
        mulheres_menor_20 += 1
    if continuar == 'N':
        break
    
print(f'{maioridade} pessoas maiores de 18.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Ao todos temos {mulheres_menor_20} mulheres com menos de 20 anos!')


maior_valor = None
nome_maior = None
maior_mil = 0
total_gasto = 0 
print('='*30)
print('Loja do Miguel :)')
print('='*30)
while True:
    nome_produto = str(input('Qual o nome do produto ? '))
    valor_produto = float(input('Qual o valor do produto ? '))
    con = input('Quer continuar [S/N]? ').strip() .upper()
    while True:
        if con in ('S' , 'N'):
            break
        print('Resposta invalida! Por favor tente novamente.')
        con = input('Quer continuar [S/N]? ').strip() .upper()
    total_gasto += valor_produto
    if valor_produto > 1000:
        maior_mil += 1
    if nome_maior is None or maior_valor < valor_produto:
        nome_maior = nome_produto
        maior_valor = valor_produto

    if con in 'N':
        break

print(f'O total gasto nas compras é de R$ {total_gasto:.2f}.')
print(f'A quantidade de produtos valendo mais de R$ 1000,00 é {maior_mil}')   
print(f'O produto mais caro é {nome_maior} custando R${maior_valor:.2f}')
'''


print('='*30)
print('Banco do Miguel:)')
print('='*30)
ciquenta = vinte = dez = um = resto = 0 
while True:
    valor_saque = int(input('Digite o valor que vc quer sacar? R$ '))
    if valor_saque == 0:
        break
    resto = valor_saque
    ciquenta = valor_saque // 50
    print(f'Vai receber {ciquenta:.0f} de R$ 50:00')
    resto %= 50
    vinte = resto // 20 
    print(f'Vai receber {vinte:.0f} notas de R$ 20:00')
    resto %= 20
    dez = resto // 10 
    print(f'Vai receber {dez:.0f} notas de R$ 10:00')
    resto %= 10 
    um = resto // 1  
    print(f'Vai receber {um:.0f} notas de R$ 01:00')  
    break
