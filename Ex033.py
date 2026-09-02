primeiroNumeroDigitado = int(input('Digite o primeiro valor: '))
segundoNumeroDigitado = int(input('Digite o segundo valor: '))
terceiroNumeroDigitado = int(input('Digite o terceiro valor: '))

maior = max(primeiroNumeroDigitado, segundoNumeroDigitado, terceiroNumeroDigitado)
menor = min(primeiroNumeroDigitado, segundoNumeroDigitado, terceiroNumeroDigitado)
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))

if primeiroNumeroDigitado > segundoNumeroDigitado and primeiroNumeroDigitado > terceiroNumeroDigitado and segundoNumeroDigitado > terceiroNumeroDigitado:
    print(primeiroNumeroDigitado)
    print(terceiroNumeroDigitado)
elif primeiroNumeroDigitado > segundoNumeroDigitado and primeiroNumeroDigitado > terceiroNumeroDigitado and segundoNumeroDigitado < terceiroNumeroDigitado:
    print(primeiroNumeroDigitado)
    print(segundoNumeroDigitado)
elif segundoNumeroDigitado > primeiroNumeroDigitado and segundoNumeroDigitado > terceiroNumeroDigitado and primeiroNumeroDigitado > terceiroNumeroDigitado:
    print(segundoNumeroDigitado)
    print(terceiroNumeroDigitado)
elif segundoNumeroDigitado > primeiroNumeroDigitado and segundoNumeroDigitado > terceiroNumeroDigitado and primeiroNumeroDigitado > terceiroNumeroDigitado:
    print(segundoNumeroDigitado)
    print(segundoNumeroDigitado)
elif terceiroNumeroDigitado > primeiroNumeroDigitado and terceiroNumeroDigitado > segundoNumeroDigitado and primeiroNumeroDigitado > segundoNumeroDigitado:
    print(terceiroNumeroDigitado)
    print(segundoNumeroDigitado)
else:
    print(terceiroNumeroDigitado)
    print(primeiroNumeroDigitado)
