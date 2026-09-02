soma_idade = 0
media_idade = 0
idade_homem_mais_velho = 0
total_mulheres_menos_vinte_anos = 0
homem_mais_velho = ''

for i in range(1, 4+1):
    print('----- {}ª pessoa -----'.format(i))
    nome = str(input('Nome: ' )).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma_idade += idade
    
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_vinte_anos += 1
        
media_idade = soma_idade / 4
print('A média de idade do grupo é {:.1f} anos'.format(media_idade))
print('O homem mais velho é o {}, com {} anos'.format(homem_mais_velho,idade_homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulheres_menos_vinte_anos))