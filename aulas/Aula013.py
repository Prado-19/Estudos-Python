lanche = ['arroz', 'feijão', 'carne', 'suco']
for i in lanche:
    print(i, end=' ')
print()

# append → adiciona item na última posição
lanche.append('macarrão')
for i in lanche:
    print(i, end=' ')
print()

# insert → adiciona item em uma posição especifica
lanche.insert(1, 'refri')
for i in lanche:
    print(i, end=' ')
print()

# del → remove item em uma posição especifica
del lanche[5]
for i in lanche:
    print(i, end=' ')
print()

# pop → remove item em uma posição especifica
lanche.pop(1)
for i in lanche:
    print(i, end=' ')
print()

# remove → remove o valor indicado
lanche.remove('arroz')
for i in lanche:
    print(i, end=' ')
print()

valores = list(range(1, 11))
# .sort() → ordena os valores de uma lista em ordem crescente
# .sort(reverse = True) → ordena os valores de uma lista em ordem decrescente
print(len(valores)) # len → quantos valores tem na lista
for i in valores:
    print(i, end=' ')
print()

for pos, v in enumerate(valores):
    print(f'pos[{pos}]: {v}')

a = [1, 4, 8, 3]
b = a
b[1] = 7
print(f'Lista A: {a}')
print(f'Lista b: {b}')

a = [1, 4, 8, 3]
b = a[:]
b[1] = 7
print(f'Lista A: {a}')
print(f'Lista b: {b}')

valores_lista = []
for i in range(0, 5):
    valores_lista.append(int(input('Digite um valor: ')))

for i in valores_lista:
    print(f'{i}...')
