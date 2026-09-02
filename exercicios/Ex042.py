ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA == ladoB == ladoC:
        print('Formou um triângulo EQUILÁTERO')
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print('Formou um triângulo ESCALENO')
    else:
        print('Formou um triângulo ISÓSCELES')
else:
    print('NÃO pode formar um triângulo')