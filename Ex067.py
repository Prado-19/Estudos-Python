while True:
    qual_tabuada = int(input('Quer ver qual Tabuada: '))
    print('~'*25)
    if qual_tabuada <= 0:
        break
    for i in range(1,11):
        print(f'{qual_tabuada} x {i} = {qual_tabuada * i}')
    print('~'*25)
print('Programa encerrado')