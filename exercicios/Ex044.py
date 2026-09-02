print('{:=^40}'.format(' Loja' ))
valorCompras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção: '))
if  opcao == 1:
    valorComDesconto = valorCompras - (valorCompras * 0.10)
    print('O valor das compras com 10% de desconto ficou em R${}'.format(valorComDesconto))
elif opcao == 2:
    valorComDesconto = valorCompras - (valorCompras * 0.05)
    print('O valor das compras com 5% de desconto ficou em R${}'.format(valorComDesconto))
elif opcao == 3:
    valorParcelado = valorCompras / 2
    print('O valor das comprar ficou R${} em duas vezes'.format(valorParcelado))
elif opcao == 4:
    qtdParcelas = int(input('Quantas parcelas: '))
    valorComJuros = valorCompras + (valorCompras * 0.20)
    valorParcelado = valorComJuros / qtdParcelas
    print('Sua compra de R${} em 10x com juros vai custar R${} por mês'.format(valorCompras,valorParcelado))
else:
    print('Opção inválida. Tente novamente!')
