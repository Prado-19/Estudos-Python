# Tipos Primitivos
# int, float, bool, str
# int <- 7, 9, 10830, -2830
# float <- 31.94, 0803.89, -3803.03231, 7.0
# boll <- True, False
# str <- 'Olá', '7.0', '7', ''

primeiroNumero = int(input('Digite um número '))
segundoNumero = int(input('Digite mais um número '))
terceiroNumero = int(input('Digite mais um número '))
resultadoSomaPrimeiroNumeroSegundoNumeroMenosTerceiroNumero = primeiroNumero + segundoNumero - terceiroNumero
print('A soma entre {} e {} menos {} é: {}'.format(primeiroNumero, segundoNumero, terceiroNumero, resultadoSomaPrimeiroNumeroSegundoNumeroMenosTerceiroNumero))

n = input('digite algo ')
print(n.isalnum())
print(n.isalpha())
print(n.isascii())
print(n.isnumeric())

