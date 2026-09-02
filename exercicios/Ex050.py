soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Contador Pares {}'.format(cont))
print('Soma {}'.format(soma))
