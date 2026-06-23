#frase é uma cadeia de caracteres/String  
frase = 'Curso em Video Python' 
frase[9]
#isso é um fatiamento
frase[9:13]
#pega as caracteres de nove ate um a menos, nesse exxemplo ele vai para o 12
frase[9:13:2]
#o ultimo numero é para pular, nesse caso de dois em dois 
frase[:5]
#nesse caso ele vem do zero ate o numero indicado 
frase[15:]
#começa do numero indicado e vai ate o final 
frase[9::3]
#vai começar no nove e vai ate o final, ja o ultimo é para pular de tres em tres

#len=comprimento da frase 
len(frase)
frase.count('o')
# vai contar quantas vezes vai aparecer a letra
# frase.count('o',0,13) indicar de onde ate onde é para contar a quantidade 
frase.find('deo')
#mostra em que momento começa a palavra em posição 
frase.find('Android')
#vai te retorna um valor negativo, dizendo que não tem essa palavra na função 
'Curso'in frase  
frase.replace('Python','Android')
#vai substituir a palavra python por android, ou seja vai procurar a primeira palavra e substituir pela segunda
frase.upper()
#as letras minusulas vai ficar maiusculas
frase.lower()
#faz o contrario 
frase.capitalize()
#vai deixar a primeira letra maiusculas e o resto minuscula 
frase.title()
# vai fazer a mesma função do capitalize mas so que com cada palavra 
frase.strip()
#remolver os espaços no começo e no final para que considere apenas as letras, ou seja o conteudo importante 
frase.split()
#duvisão onde tem espaço 
'-'.join(frase)
#vai juntar as string separada e mostrar entre elas o que ta antes do ponto join 
