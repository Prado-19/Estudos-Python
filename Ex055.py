maior_peso = 0
menor_peso = 0
for i in range(1, 5+1):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi {}Kg'.format(maior_peso))
print('O menor peso lido foi {}Kg'.format(menor_peso))