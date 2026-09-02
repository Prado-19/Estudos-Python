print('='*30)
print('{: ^30}'.format('Banquinho'))
print('='*30)
valor = int(input('Qual valor deseja sacar: R$'))
cinquenta = valor // 50
resto = valor % 50
vinte = resto // 20
resto %= 20
dez = resto // 10
resto %= 10

if cinquenta != 0:
    print(cinquenta)
if vinte != 0:
    print(vinte)
if dez != 0:
    print(dez)
if resto != 0:
    print(resto)

total = valor
cedula = 50
qtd_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        qtd_cedula += 1
    else:
        if qtd_cedula > 0:
            print(f'Total de {qtd_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        qtd_cedula = 0
        if total == 0:
            break
