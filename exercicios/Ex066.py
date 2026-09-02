qtd_num = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qtd_num += 1
print(f'A soma dos {qtd_num} é {soma}.')