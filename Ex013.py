salarioInicial = float(input('Qual é o salário do funcionário? R$'))
salarioComAumento = salarioInicial + (salarioInicial * 15/100)
print('Um funcioonário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salarioInicial,salarioComAumento))