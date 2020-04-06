from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto,adjacente)
print('O Comprimento da hipotenusa é = {:.2f}'.format(hipotenusa))