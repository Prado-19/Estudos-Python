from datetime import date
anoDigitado = int(input('Qual ano o programa deve analizar? Se desejar analizar o ano atual digite 0: '))
if anoDigitado == 0:
    anoDigitado = date.today().year
if anoDigitado % 4 == 0 and anoDigitado % 100 != 0 or anoDigitado % 400 == 0:
    print('{} é um ano bissexto!'.format(anoDigitado))
else:
    print('{} não é ano bissexto!'.format(anoDigitado))