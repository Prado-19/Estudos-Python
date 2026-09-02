frase = input('Digite algo: ').strip().upper()
palavras = frase.split()
frase_junta = ''.join(palavras)
frase_invertida = frase_junta[::-1]

print('A frase {} invertida é {}'.format(frase_junta, frase_invertida))
if frase_junta == frase_invertida:
    print('É um PALINDROMO')
else:
    print('NÃO é um PALINDROMO')