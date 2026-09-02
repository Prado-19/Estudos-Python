from datetime import date
anoNascimento = int(input('Em qual ano você nasceu: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Quem nasceu em {}, no ano de {} tem {} anos'.format(anoNascimento, anoAtual, idade))
if anoAtual - anoNascimento > 18:
    print("Você deveria ter se alistado a {} anos".format(idade - 18))
    print("Seu alistamento ocorreu em {}".format(anoAtual - abs(idade - 18)))
elif anoAtual - anoNascimento < 18:
    print("Você deverá se alistar daqui a {} anos".format(abs(idade - 18)))
    print("Em {}".format(anoAtual + abs(idade - 18)))
else:
    print("Você deve se alistar IMEDIATAMENTE")
