from time import sleep
primeiro_num = int(input('Primeiro número: '))
segundo_num = int(input('Segundo número: '))
opcao = 0
while opcao != 6:
    print('=-'*30)
    sleep(0.5)
    print('{:^15}'.format('OPÇÕES'))
    print('[ 1 ]    SOMAR')
    print('[ 2 ]    SUBTRAIR')
    print('[ 3 ]    MULTIPLICAR')
    print('[ 4 ]    MAIOR')
    print('[ 5 ]    MENOR')
    print('[ 6 ]    SAIR DO PROGRAMA')
    opcao = int(input('>>> Qual a opção desejada: '))
    print('=-'*30)
    if opcao == 1:
        soma = primeiro_num + segundo_num
        print('A soma entre o primeiro e o segundo número é: {}'.format(soma))
    elif opcao == 2:
        subtracao = primeiro_num - segundo_num
        print('A subtração entre o primeiro e o segundo número é: {}'.format(subtracao))
    elif opcao == 3:
        multiplicacao = primeiro_num * segundo_num
        print('A multiplicação entre o primeiro e o segundo número é: {}'.format(multiplicacao))
    elif opcao == 4:
        if primeiro_num > segundo_num:
            maior = primeiro_num
            print('O maior valor entre o primeiro e o segundo número é: {}'.format(maior))
        else:
            maior = segundo_num
            print('O maior valor entre o primeiro e o segundo número é: {}'.format(maior))
    elif opcao == 5:
        if primeiro_num > segundo_num:
            menor = segundo_num
            print('O menor valor entre o primeiro e o segundo número é: {}'.format(menor))
        else:
            menor = primeiro_num
            print('O menor valor entre o primeiro e o segundo número é: {}'.format(menor))
    elif opcao == 6:
        print('Finalizando...')
    else:
        print('Opção Inválida')
sleep(1)
print('Fim do Programa')