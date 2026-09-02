continuar = 'S'
soma = 0
qtd_num = 0
maior = menor = 0
while continuar in 'S':
    num = int(input('Digite um número: '))
    soma += num
    qtd_num += 1
    if qtd_num == 1:
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
print('Você digitou {} número e a média é {:.2f}'.format(qtd_num, (soma / qtd_num)))
print('O menor valor é {} e o maior valor é {}'.format(menor, maior))
