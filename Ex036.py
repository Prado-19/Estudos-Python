valorDaCasa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anosParaPagar = int(input('Em quantos anos você ira pagar: '))
prestacaoMensal = valorDaCasa / (anosParaPagar * 12)
trintaPorcentoDoSalario = salario * 0.30
if prestacaoMensal > trintaPorcentoDoSalario:
    print('Empréstimo NEGADO')
else:
    print('Emprestimo CONCEDIDO para pagar a casa no valor de R${:.2f}, cada prestação vai custar R${:.2f} por mês'.format(valorDaCasa, prestacaoMensal))