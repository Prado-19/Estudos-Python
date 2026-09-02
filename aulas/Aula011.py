i = 1
num = 0
soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
print('A soma é {}'.format(soma)) # nova formatação do print Python 3
print(f'A soma é {soma}') # nova formatação do print Python 3.6+
print('A soma é %d'%(soma)) # formatação do print python 2

'''while num != 999:
    num = int(input('Digite um número: '))
    soma += num
print(soma)

while i <= 10:
    print(i, end=' ')
    i += 1
print('Fim')'''
