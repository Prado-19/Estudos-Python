soma = 0
contador = 0
for i in range(3, 501, 3):
    if i % 2 != 0:
        contador += 1
        soma += i
print('Quantidade de valores solicitados é {}'.format(contador))
print('A soma é: {}'.format(soma))
