from datetime import date
maior_idade = 0
menor_idade = 0
ano_atual = date.today().year
for i in range(1, 7+1):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    if ano_atual - ano_nascimento >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior_idade))
print('Ao todo tivemos {} pessoa menores de idade'.format(menor_idade))