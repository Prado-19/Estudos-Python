cidadeDeNascimentoDigitadoPeloUsuario = input('Digite em qual cidade você nasceu: ').strip()
print(cidadeDeNascimentoDigitadoPeloUsuario[:5].upper() == 'SANTO')
print('SANTO' in cidadeDeNascimentoDigitadoPeloUsuario[:5].upper())