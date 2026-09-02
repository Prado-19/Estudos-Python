lanche = ('Habúrguer', 'Suco', 'Pizza', 'Pudim', 'Amido de Milho')
# tuplas são imutaveis
# lanche[1] = 'Refri'

pessoa = ('Daniel', 16, 'M', 70.10)
print(pessoa)

print(pessoa)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (a + b)
print(c)
print(c.count(2))
print(c.index(5))

print(len(lanche))
for i in range(0, len(lanche)):
    print(lanche[i], end=' ')
print()
for i in lanche:
    print(i, end=' ')
print()
print(lanche[1:3])
print(lanche[0:])
print(lanche[3])
print(lanche[-2])
print(lanche[-2:])

for pos, i in enumerate(lanche):
    print(i, pos)
    
print(sorted(lanche))

