import math
angulo = float(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,coseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
