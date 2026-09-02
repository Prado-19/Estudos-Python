num = 1
qtd_num = 0
soma = 0
while num != 0:
    num = int(input('Digite um número [0 para parar]: '))
    if num != 0:
        qtd_num += 1
        soma += num
print('Você digitou {} número e a soma foi {}'.format(qtd_num, soma))
