salarioDigitado = float(input('Qual o salário do funcionário: R$'))
if salarioDigitado <= 5000.00:
    reajunteSalarial = salarioDigitado + (salarioDigitado * 0.15)
    print('O salário com reajuste de 15% é {:.2f}'.format(reajunteSalarial))
else:
    reajunteSalarial = salarioDigitado + (salarioDigitado * 0.10)
    print('O salário com reajuste de 10% é {:.2f}'.format(reajunteSalarial))
