velocidadeDoCarroDigitada = float(input('Qual a velocidade do carro: '))
if velocidadeDoCarroDigitada > 80:
    valorDaMulta = (velocidadeDoCarroDigitada - 80) * 7
    print('MULTADO! Você ultraprassou o limite de 80Km/h, terá de pagar R${:.2f}'.format(valorDaMulta))
print('Tenha um bom dia, dirija com cuidado!')
