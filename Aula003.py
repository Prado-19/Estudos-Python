nome = input('Qual seu nome? ')
print('Bem-vindo(a) ao meu programa {:-^20}'.format(nome))

primeiroNumero = int(input('Dgite um número '))
segundoNumero = int(input('Dgite um número '))
somaEntrePrimeiroNumeroSegundoNumero = primeiroNumero + segundoNumero
subtracaoEntrePrimeiroNumeroSegundoNuemro = primeiroNumero - segundoNumero
multiplicacaoEntrePrimeiroNumeroSegundoNumero = primeiroNumero * segundoNumero
divisaoEntrePrimeiroNumeroSegundoNumero = primeiroNumero / segundoNumero
divisaoInteiraEntrePrimeiroNumeroSegundoNumero = primeiroNumero // segundoNumero
potenciacaoEntrePrimeiroNumeroSegundoNumero = primeiroNumero ** segundoNumero

print('A soma é {}\nA subtração é {}\nA multiplicação é {}\nA divisão é {:.3f}\nA divisão Inteira é {}\nA potenciação é {}'.format(somaEntrePrimeiroNumeroSegundoNumero, subtracaoEntrePrimeiroNumeroSegundoNuemro, multiplicacaoEntrePrimeiroNumeroSegundoNumero, divisaoEntrePrimeiroNumeroSegundoNumero, divisaoInteiraEntrePrimeiroNumeroSegundoNumero, potenciacaoEntrePrimeiroNumeroSegundoNumero))
