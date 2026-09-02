modeloCarroDigitado = str(input('Qual o seu carro: '))
if modeloCarroDigitado == "Ferrari spider":
    print('Você tem uma Ferrari')
elif modeloCarroDigitado == "Porche 911":
    print('Você tem um Porche')
elif modeloCarroDigitado == "BMW Q3" or modeloCarroDigitado == "BMW Q2" or modeloCarroDigitado == "BMW Q5":
    print('Você tem um BMW')
else:
    print('Modelo não identificado')  
print('Tenha um bom dia, digija com cuidado!')