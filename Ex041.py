from datetime import date
dataNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - dataNascimento

print('O atleta tem {} anos'.format(idade))
if idade > 25:
    print('Categoria MASTER')
elif idade > 19:
    print('Categoria SENIOR')
elif idade > 14:
    print('Categoria JUNIOR')
elif idade > 9:
    print('Categoria INFANTIL')
else:
    print('Categoria MIRIM')
