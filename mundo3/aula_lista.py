# Criando uma lista com alguns caracteres
lista = ['m', 'j', 'k', 'l', 's']

# Adiciona o elemento 'i' no FINAL da lista
lista.append('i')

# Insere o elemento 'q' na posição 0 (início da lista)
lista.insert(0, 'q')

# Remove o elemento que está na posição 3
del lista[3]

# Remove e retorna o elemento da posição 3
lista.pop(3)

# Remove o PRIMEIRO elemento com valor 'm'
lista.remove('m')

# Mostra o estado final da lista
print(lista)


# Criando uma lista com números inteiros
valores = [0, 2, 3, 8, 4, 6, 10, 9, 7, 10]

# Ordena a lista em ordem crescente
valores.sort()
print(valores)

# Ordena a lista em ordem decrescente
valores.sort(reverse=True)

# Remove o último elemento da lista
valores.pop()

# Percorre a lista mostrando os valores
for v in valores:
    print(f'{v}...', end='')

print()  # Apenas para quebrar linha

# Percorre a lista mostrando posição (c) e valor (v)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')


# Criando uma lista vazia
valores = []

# Laço para adicionar 4 valores digitados pelo usuário
for cont in range(1, 5):
    valores.append(int(input('Digite um valor: ')))

# Mostra os valores digitados
for v in valores:
    print(f'{v}...', end='')

print()  # Quebra de linha


# Quando se iguala uma lista à outra, o Python cria uma LIGAÇÃO entre elas
a = [2, 3, 4, 4]

# b recebe a MESMA lista de a (ligação)
b = a

# b recebe uma CÓPIA da lista a (listas independentes)
b = a[:]


#Lista parte dois 

pessoas = []
dados = ['Pedro', 25]
pessoas.append(dados[:])

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 19]]
print(pessoas[1]) or print(pessoas[0][0])


teste = []

teste.append('Miguel')
teste.append(40)
galera = []

galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


pessoas = [['Miguel', 16], ['Gustavo', 20], ['João', 30], ['Alura', 40]]

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

totalmai = totalmen = 0
galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmen += 1

print(f'A quantidade de maior de idade é {totalmai} e a quantidade de menor é {totalmen}')



# Criando uma lista com alguns caracteres
lista = ['m', 'j', 'k', 'l', 's']

# Adiciona o elemento 'i' no final da lista
lista.append('i')

# Insere o elemento 'q' na posição 0 da lista
lista.insert(0, 'q')

# Remove o elemento que está na posição 3 da lista
del lista[3]

# Remove e retorna o elemento da posição 3 da lista
lista.pop(3)

# Remove o primeiro elemento da lista que tenha o valor 'm'
lista.remove('m')

# Mostra a lista após todas as operações acima
print(lista)


# Criando uma lista com números inteiros
valores = [0, 2, 3, 8, 4, 6, 10, 9, 7, 10]

# Ordena os valores da lista em ordem crescente
valores.sort()
print(valores)

# Ordena os valores da lista em ordem decrescente
valores.sort(reverse=True)

# Remove o último elemento da lista
valores.pop()

# Percorre a lista e mostra cada valor
for v in valores:
    print(f'{v}...', end='')

# Quebra de linha
print()

# Percorre a lista mostrando a posição (c) e o valor (v)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')


# Criando uma lista vazia
valores = []

# Laço que executa 4 vezes
for cont in range(1, 5):
    # Lê um número digitado pelo usuário e adiciona na lista
    valores.append(int(input('Digite um valor: ')))

# Mostra os valores digitados
for v in valores:
    print(f'{v}...', end='')

# Quebra de linha
print()


# Criando uma lista com alguns números
a = [2, 3, 4, 4]

# b passa a apontar para a mesma lista que a
b = a

# b recebe uma cópia da lista a
b = a[:]


# Inicializa os contadores de maiores e menores de idade
totalmai = totalmen = 0

# Lista que vai armazenar os dados das pessoas
galera = []

# Lista auxiliar para armazenar nome e idade temporariamente
dado = []

# Laço que executa 3 vezes
for c in range(0, 3):
    # Lê o nome e adiciona na lista dado
    dado.append(str(input('Nome: ')))

    # Lê a idade e adiciona na lista dado
    dado.append(int(input('Idade: ')))

    # Adiciona uma cópia da lista dado dentro da lista galera
    galera.append(dado[:])

    # Limpa a lista dado para reutilizar no próximo loop
    dado.clear()

# Mostra a lista completa de pessoas
print(galera)

# Percorre a lista galera
for p in galera:
    # Verifica se a idade é maior ou igual a 21
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmen += 1

# Mostra a quantidade de maiores e menores de idade
print(f'A quantidade de maior de idade é {totalmai} e a quantidade de menor é {totalmen}')
