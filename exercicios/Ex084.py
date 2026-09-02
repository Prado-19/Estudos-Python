galera = []
nomePeso = []
maiorPeso = menorPeso = 0
while True:
    nomePeso.append(str(input('Nome: ')))
    nomePeso.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorPeso = menorPeso = nomePeso[1]
    else:
        if nomePeso[1] < menorPeso:
            menorPeso = nomePeso[1]
        elif nomePeso[1] > maiorPeso:
            maiorPeso = nomePeso[1]
    galera.append(nomePeso[:])
    nomePeso.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('[S/N]')).upper().strip()[0]
    if opcao in 'N':
        break
print('=-'*25)
print(f'O total de pessoas cadastrados foi {len(galera)}')
print(f'O maior peso é {maiorPeso}Kg.', end=' ')
for i in galera:
    if i[1] == maiorPeso:
        print(i[0], end=' ')
print()
print(f'O menor peso é {menorPeso}Kg.', end=' ')
for i in galera:
    if i[1] == menorPeso:
        print(i[0], end=' ')
print()

'''
Ana
75.5
s
Pedro
89
s
Joana
89
s
Carolina
55
s
Bianca
55
n
'''
