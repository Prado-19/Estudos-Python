sexo = str(input('Informe seu sexo [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dado Inválido. Digite novamente [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))