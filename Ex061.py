primeiro_termo = int(input('1° termo: '))
razao = int(input('Razão: '))

i = 1
while i <= 10:
    num = primeiro_termo + (i - 1) * razao
    print(num, end=' → ')
    i += 1
print('Fim do programa')
