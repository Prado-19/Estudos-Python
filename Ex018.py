from math import sin, cos, tan, radians
numeroDigitado = float(input('Digite o ângulo que você deseja: '))
radianosDoNumeroDigitado = radians(numeroDigitado)
senoDoNumeroDigitado = sin(radianosDoNumeroDigitado)
cossenoDoNumeroDigitado = cos(radianosDoNumeroDigitado)
tangenteDoNumeroDigitado = tan(radianosDoNumeroDigitado)
print('O ângulo de {}° tem o Seno de {:.2f}'.format(numeroDigitado,senoDoNumeroDigitado))
print('O ângulo de {}° tem o Cosseno de {:.2f}'.format(numeroDigitado,cossenoDoNumeroDigitado))
print('O ângulo de {}° tem a Tangente de {:.2f}'.format(numeroDigitado,tangenteDoNumeroDigitado))