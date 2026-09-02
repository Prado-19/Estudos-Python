nomeInteiroDigitado = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nomeInteiroDigitado.upper()))
print('Seu nome em minúscula é {}'.format(nomeInteiroDigitado.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nomeInteiroDigitado) - nomeInteiroDigitado.count(' ')))
primeiroNome = nomeInteiroDigitado.split()[0]
print('Seu primeiro nome é {} e tem {} letras'.format(primeiroNome, len(primeiroNome)))