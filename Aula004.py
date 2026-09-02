# import bebidas <- importa todas todas as funcionalidades do modulo
# from bedidas import agua <- importa somente a funcionalidade especifica

from math import sqrt
import math
import random

numeroDaMaquina = random.randint(1,100)
print(numeroDaMaquina)

numeroDigitado = int(input('Digite um número: '))
potenciaDoNumeroDigitado = int(math.pow(numeroDigitado, 2))
raizQuadradaDoNumeroDigitado = sqrt(numeroDigitado)
print('A raiz quadrade de {} = {:.3f}'.format(numeroDigitado,raizQuadradaDoNumeroDigitado))
print('E a potência de {} = {}'.format(numeroDigitado,potenciaDoNumeroDigitado))