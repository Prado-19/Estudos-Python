num = int(input('Digite um número: '))
print('1 - Binário')
print('2 - Octal')
print('3 - hexadecimal')
operacao = int(input('Qual operação deseja fazer: '))

if operacao == 1:
    print('{} = {} em BINÁRIO'.format(num, bin(num)[2:]))
elif operacao == 2:
    print('{} = {} em OCTAL'.format(num, oct(num)[2:]))
elif operacao == 3:
    print('{} = {} em HEXADECIMAL'.format(num, hex(num)[2:]))
else:
    print('Opcão invalida')
