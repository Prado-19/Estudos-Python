print('-'*20)
print('{: ^20}'.format('Loja Meio-Barata'))
print('-'*20)
valor_compra = produtos_mais_de_mil = menor_preco = i = 0
nome_produto_menor_preco = ''
while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    valor_compra += preco
    if preco > 1000:
        produtos_mais_de_mil += 1
    if i == 0:
        menor_preco = preco
        nome_produto_menor_preco = nome_produto
    if preco < menor_preco:
        menor_preco = preco
        nome_produto_menor_preco = nome_produto
    i += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-'*20)
print(f'O total da compra é R${valor_compra}')
print(f'Temos {produtos_mais_de_mil} custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto_menor_preco} que custou R${menor_preco}')