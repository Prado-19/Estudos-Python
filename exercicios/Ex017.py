from math import pow, sqrt, hypot

catetoOposto = float(input('Qual o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Qual o comprimento do cateto adjacente: '))
somaCatetoOpostoCatetoAdjacenteAoQuadrado = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)
hipotenusa01 = sqrt(somaCatetoOpostoCatetoAdjacenteAoQuadrado)
hipotenusa02 = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa é {:.2f}'.format(hipotenusa01))
print('A hipotenusa é {:.2f}'.format(hipotenusa02))
