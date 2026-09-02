lista = [[], []]
for i in range(1, 8):
    num = int(input(f'{i}°: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Valores pares: {lista[0]}')
print(f'Valores ímpares: {lista[1]}')
