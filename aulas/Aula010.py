for i in range(1, 11):
    print(i)
print('FIM')

i = 11
while i <= 20:
    print(i)
    i +=1
print('FIM')


for i in range(1, 3):
    num1 = int(input('{}° valor: '.format(i)))
print('FIM')

i = 1
qtdPares = 0
qtdImpares = 0
num = int(input('Digite um valor diferente de zero para começar: '))
while num != 0:
    num = int(input('{}° valor: '.format(i)))
    if num != 0:
        if num % 2 == 0:
            qtdPares += 1
        else:
            qtdImpares += 1
    i += 1
print('Quantidade de PARES: {}'.format(qtdPares))
print('Quantidade de IMPARES: {}'.format(qtdImpares))
print('FIM')