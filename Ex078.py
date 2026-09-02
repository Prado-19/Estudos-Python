valores = []
maior_posicao = []
menor_posicao = []
maior = menor = cont = 0

for i in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição [{i}]: ')))
    if i == 0:
        menor = maior = valores[i]
    else:
        if valores[i] < menor:
            menor = valores[i]
        if valores[i] > maior:
            maior = valores[i]

for pos, i in enumerate(valores):
    if i == menor:
        menor_posicao.append(pos)
    elif i == maior:
        maior_posicao.append(pos)

print('=-'*25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}, nas posição {maior_posicao}')
print(f'O menor valor digitado foi {menor}, nas posição {menor_posicao}')
