diasDoCarroAlugado = int(input('Quantos dias alugados? '))
quilometrosRodados = float(input('Quantos km rodados? '))
valorPagarPeloAluguel = (60 * diasDoCarroAlugado) + (0.15 *  quilometrosRodados)
print('O total a pagar é de R${:.2f}'.format(valorPagarPeloAluguel))
