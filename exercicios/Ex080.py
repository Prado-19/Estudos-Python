numero = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > numero[-1]:
        numero.append(num)
        print(f'{num} foi adicionado na última posição')
    else:
        pos = 0
        while pos < len(numero):
            if num <= numero[pos]:
                numero.insert(pos, num)
                print(f'{num} foi adicionado na posição {pos}')
                break
            pos += 1
print(numero)
