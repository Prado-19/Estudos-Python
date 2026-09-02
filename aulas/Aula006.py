idade = 17
if idade >= 18:
    print('Maior de idade')
else:
    print('Ainda não é maior de idade')
print('...FIM...')

nomeDigitadoPeloUsuario = input('Digite seu nome: ')
if nomeDigitadoPeloUsuario == 'Isabeli':
    print('Seu nome é perfeito, você é muito linda {}'.format(nomeDigitadoPeloUsuario))
print('Oi {}'.format(nomeDigitadoPeloUsuario))

nota01 = float(input('Nota 01: '))
nota02 = float(input('Nota 02: '))
media = (nota01 + nota02) / 2
if media >= 7.0:
    print('Eba você passou de ano')
else:
    print('Você não passou de ano .-.')