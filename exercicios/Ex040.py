nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('O aluno esta APROVADO com media {:.1f}'.format(media))
elif media < 5:
    print('O aluno esta REPROVADO com media {:.1f}'.format(media))
else:
    print('O aluno esta de RECUPERAÇÃO com media {:.1f}'.format(media))
