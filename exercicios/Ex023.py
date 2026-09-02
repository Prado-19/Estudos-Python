numeroDigitadoPeloUsuario = int(input('Informe um número: '))
unidadeDoNumeroDigitadoPeloUsuario = numeroDigitadoPeloUsuario // 1 % 10
dezenaDoNumeroDigitadoPeloUsuario = numeroDigitadoPeloUsuario // 10 % 10
centenaDoNumeroDigitadoPeloUsuario = numeroDigitadoPeloUsuario // 100 % 10
milharDoNumeroDigitadoPeloUsuario = numeroDigitadoPeloUsuario // 1000 % 10
print('Analizando o número {}'.format(numeroDigitadoPeloUsuario))
print('Possui {} unidade(s)'.format(unidadeDoNumeroDigitadoPeloUsuario))
print('Possui {} dezena(s)'.format(dezenaDoNumeroDigitadoPeloUsuario))
print('Possui {} centena(s)'.format(centenaDoNumeroDigitadoPeloUsuario))
print('Possui {} milhar(res)'.format(milharDoNumeroDigitadoPeloUsuario))
