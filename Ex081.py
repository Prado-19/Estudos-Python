numero = []
while True:
    numero.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Você digitou {len(numero)} valores')
numero.sort(reverse=True)
print(f'Os valores em forma decrescente são {numero}')
if 5 in numero:
    print('Tem  o número 5')
else:
    print('Não tem o número 5')
