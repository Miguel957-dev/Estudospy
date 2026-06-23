# Tuplas -> Variáveis Composta 

lanche = 'Hambúrguer', 'suco', 'pizza', 'pudim'
'''print(lanche[:4]) 

#AS TUPLAS SÃO IMUTÁVEIS 
for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

'''

print(sorted(lanche))

a = (2, 5, 4)
b = (2, 6, 3, 7, 5)
c = a + b
print(c.count(5))# Conta quantas vezes aparece o número informado 
print(c.index(2, 2))# Mostra em qual posição ta o número informado



