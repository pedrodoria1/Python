n1 = int(input('Digite o número limite: ')) #Solicitando ao usuário o número limite.
count3 = 0 #Criei um contador para cada multiplo.
count5 = 0
count2 = 0
count8 = 0
c = 3
for c in range(n1+1): #Aqui faço as operações para cada contador.
    if (c%3)==0:
        if c==0:
            continue
        print ('Os múltiplos de 3 abaixo de {} limite: {}'.format(n1,c))
        count3 = count3+c
print('A soma dos valores é: {}'.format(count3))

for c in range(n1+1):
    if (c%5)==0:
        if c==0:
            continue
        print ('Os múltiplos de 5 abaixo de {} limite: {}'.format(n1,c))
        count5 = count5+c
print('A soma dos valores é: {}'.format(count5))

for c in range(n1+1):
    if (c%2)==0:
        if c==0:
            continue
        print ('Os múltiplos de 2 abaixo de {} limite: {}'.format(n1,c))
        count2 = count2+c
print('A soma dos valores é: {}'.format(count2))

for c in range(n1+1):
    if (c%8)==0:
        if c==0:
            continue
        print ('Os múltiplos de 8 abaixo de {} limite: {}'.format(n1,c))
        count8 = count8+c
print('A soma dos valores é: {}'.format(count8))