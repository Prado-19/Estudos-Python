num_digitado = int(input('Digite um número: '))
qtd_de_divisoes = 0

for i in range(1, num_digitado + 1):
    if num_digitado % i == 0:
        print('{}{}{}'.format('\033[1;32m',i,'\033[m'), end=' ')
        qtd_de_divisoes += 1
    else:
        print('{}{}{}'.format('\033[1;31m',i,'\033[m'), end=' ')
print('')
print('O número {} foi divisível {} vezes'.format(num_digitado, qtd_de_divisoes))
if qtd_de_divisoes == 2:
    print('O número {} é PRIMO'.format(num_digitado))
else:
    print('O número {} NÃO é PRIMO'.format(num_digitado))
