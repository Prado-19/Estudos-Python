tamanhoEmMetros = float(input('Qual o tamanho em m? '))
tamanhoEmQuilometros = tamanhoEmMetros / 1000
tamanhoEmHectometos = tamanhoEmMetros / 100
tamanhoEmDecametros = tamanhoEmMetros / 10
tamanhoEmDecimetros = tamanhoEmMetros * 10
tamanhoEmCentimetros = tamanhoEmMetros * 100
tamanhoEmMilimetros = tamanhoEmMetros * 1000
print('{}m'.format(tamanhoEmMetros))
print('{}km, {}hm, {}dam, {}dm, {}cm, {}mm'.format(tamanhoEmQuilometros,tamanhoEmHectometos,tamanhoEmDecametros,tamanhoEmDecimetros,tamanhoEmCentimetros,tamanhoEmMilimetros))
