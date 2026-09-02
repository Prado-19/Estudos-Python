from math import trunc
numeroDigitado = float(input('Digite um núnero: '))
parteInteiraDoNumeroDigitado01 = trunc(numeroDigitado)
parteInteiraDoNumeroDigitado02 = int(numeroDigitado)
print('A parte inteira de {} é {}'.format(numeroDigitado,parteInteiraDoNumeroDigitado01))
print('A parte inteira de {} é {}'.format(numeroDigitado,parteInteiraDoNumeroDigitado02))
