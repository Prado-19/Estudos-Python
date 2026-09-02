qtd_termos = int(input('Quantos termos você quer ver: '))
a = 0
b = 1
i = 1
while i <= qtd_termos:
    print(a, end=' → ')
    c = a + b
    a = b
    b = c
    i += 1
print('Fim do programa')
