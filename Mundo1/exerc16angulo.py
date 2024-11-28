from math import radians, sin , cos, tan
ângulo = float(input('digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(' o ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))