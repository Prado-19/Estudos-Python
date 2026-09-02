print('~'*50)
print(f'{"LISTAGEM DE PREÇO": ^50}')
print('~'*50)
lista_de_produtos = ('Lápis', 1.75,
                  'Borracha', 2.00,
                  'Caneta', 2.50,
                  'Caderno', 15.90,
                  'Estojo', 25.00,
                  'Compasso', 9.99,
                  'Mochila', 120.30,
                  'Livro', 34.90)
for pos in range(0, len(lista_de_produtos)):
    if pos % 2 == 0:
        print(f'{lista_de_produtos[pos]:.<40}', end='')
    else:
        print(f'R$ {lista_de_produtos[pos]:>7.2f}')
print('~'*50)
