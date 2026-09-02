distanciaDigitada = float(input('Qual a distancia da viagem: '))
if distanciaDigitada <= 200.0:
    precoDaViagem = distanciaDigitada * 0.5
    print("O preço da viagem de {}Km é de R${}!".format(distanciaDigitada, precoDaViagem))
else:
    precoDaViagem = distanciaDigitada * 0.45
    print("O preço da viagem de {}Km é de R${}!".format(distanciaDigitada, precoDaViagem))
print("Tenha uma boa viagem!")