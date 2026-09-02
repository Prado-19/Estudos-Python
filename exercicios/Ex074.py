from random import randint
num_sorteado = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print('Os números sorteados foram:', end=' ')
for i in num_sorteado:
    print(i, end=' ')
print(f'\nO maior valor é {max(num_sorteado)}')
print(f'O menor valor é {min(num_sorteado)}')