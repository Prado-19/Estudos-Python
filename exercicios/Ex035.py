print('=-' * 11)
print('Analizando Triângulos')
print('=-' * 11)
primeiroLado = float(input('Primeiro lado: '))
segundoLado = float(input('Segundo lado: '))
terceiroLado = float(input('Terceiro lado: '))
if primeiroLado + segundoLado > terceiroLado and primeiroLado + terceiroLado > segundoLado and segundoLado + terceiroLado > primeiroLado:
    print('É possivel formar um triângulo!')
else:
    print('Não é possivel formar um triângulo!')