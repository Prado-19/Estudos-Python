primeiro_termo = int(input('1° termo: '))
razao = int(input('Razão: '))

qtd_termos = 0
fim = 0
i = 1
mais = 10
while mais != 0:
    fim += mais
    while i <= fim:
        num = primeiro_termo + (i - 1) * razao
        print(num, end=' → ')
        i += 1
        qtd_termos += 1
    print('Pausa')
    mais = int(input('Quer verificar mais quantos números: '))
print('Foram verificados os {} termos da P.A.'.format(qtd_termos))
print('Fim do programa')