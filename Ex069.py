qtd_pessoas_mais_dezoito = qtd_homens = qtd_mulher_menos_vinte = 0
while True:
    print('~'*25)
    print('Cadastre uma pessoa')
    print('~'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    print('~'*25)
    if idade > 18:
        qtd_pessoas_mais_dezoito += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulher_menos_vinte += 1
    contiunar = ' '
    while contiunar not in 'SN':
        contiunar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if contiunar == 'N':
        break
print(f'Total de pessoa com mais de 18 anos é {qtd_pessoas_mais_dezoito}')
print(f'Ao todo foram cadatrados {qtd_homens} homens')
print(f'E temos {qtd_mulher_menos_vinte} mulher com menos de 20 anos')