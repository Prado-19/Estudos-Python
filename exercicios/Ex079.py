valores = []
while True:
    num = (int(input('Digite um número: ')))
    if num not in valores:
        valores.append(num)
        print('Valor inserido com sucesso')
    else:
        print('Valor duplicado. Não vou inserir')
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
valores.sort()
print(valores)
