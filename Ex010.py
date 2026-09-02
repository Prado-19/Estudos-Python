dinheiroEmReais = float(input('Quanto dinheiro você tem na carteira? R$ '))
dinheiroEmDolars = dinheiroEmReais / 4.97
print('Com R${} você pode comprar US${:.2f}'.format(dinheiroEmReais, dinheiroEmDolars))