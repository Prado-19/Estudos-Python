primeiro_termo = int(input('1° termo: '))
razao = int(input('Razão: '))

for i in range(1, 11):
    num = primeiro_termo + (i - 1) * razao
    print(num, end=' → ')
print('Fim do programa')