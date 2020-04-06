n1 = int(input('Digite um número para ser o limite inferior: ')) #Recebendo o limite inferior.
n2 = int(input('Digite um número para ser o limite superior: ')) #Recebendo o limite superior.

'''Fazendo um laço de repetição while para exibir os números do inferior ao superior, dentro do while,
temos um if. O if valida se o resto da divisão do número que está sendo incrementado é 0, se sim, ele printa.
Desta forma, só são exibidos números pares.'''
while n1<=n2:
    if (n1%2)==0:
        print(n1)
    n1 += 1