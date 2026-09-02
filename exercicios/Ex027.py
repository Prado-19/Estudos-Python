nomeCompletoDIgitadoPeloUsuario = input('Digite seu nome completo: ').strip()
print('Analizando o nome: {}.'.format(nomeCompletoDIgitadoPeloUsuario))
print('Seu primeiro nome é {}.'.format(nomeCompletoDIgitadoPeloUsuario.split()[0]))
print('Seu último nome é {}.'.format(nomeCompletoDIgitadoPeloUsuario.split()[-1]))