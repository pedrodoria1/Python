from random import randint

#Aqui fiz a declaração da tupla. Como ela não pode ser alterada, fiz a conversão em lista para adicionar os
#números inteiros a ela de forma randômica, utilizando uma função da biblioteca random.

tupla = tuple()
lista = list(tupla)
for i in range(10):
    x = randint(-1000, 1000)
    lista.append(x)

tupla = tuple(lista)
print(tupla)

#Criei uma variável para cada questão. Essas variáveis vão receber os valores correspondentes ao que se pede na questão.
#Exemplo: impares, vai receber os valores ímpares da tupla. Com essa informação, eu faço a operação necessária para
#cada questão. No caso das ímpares foi exibir a quantidade de ímpares. Basta dar um print no length da variável ímpaeres.

impares = []
pares = []
positivos = []
negativos = []

for j in range(len(lista)):
    if lista[j] % 2 == 0:
        pares.append(j)
    else:
        impares.append(lista[j])

for k in range(len(lista)):
    if lista[k] >= 0:
        positivos.append(lista[k])
    elif lista[k] < 0:
        negativos.append(lista[k])

mediaPositivos = 0
for p in range(len(positivos)):
    mediaPositivos = mediaPositivos + positivos[p]
mediaPositivos = mediaPositivos / len(positivos)

quadradoNegativos = 0
for n in range(len(negativos)):
    quadradoNegativos = quadradoNegativos + negativos[n]
quadradoNegativos = quadradoNegativos ** 2


print('A quantidade de números ímpares: {}'.format(len(impares)))
print('As posições dos números pares: {}'.format(pares))
print('A média aritmética dos números positivos: {}'.format(mediaPositivos))
print('O quadrado da soma dos números negativos: {}'.format(quadradoNegativos))