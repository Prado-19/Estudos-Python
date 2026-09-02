'''from math import factorial
print(factorial(num))'''
num = int(input('Digite um número para calcular o fatorial: '))

print('Calculando o FATORIAL de {}'.format(num))
print('Calculando {}!'.format(num), end=' = ')
fatorial = 1
while num > 0:
    fatorial *= num
    if num != 1:
        print('{}'.format(num), end=' x ')
    else:
        print('{}'.format(num), end=' = ')
    num -= 1
print('{}'.format(fatorial))