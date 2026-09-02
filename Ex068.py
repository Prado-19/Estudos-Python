from random import randint
qtd_vitorias = 0
while True:
    print('Jogo do PAR ou Ímpar')
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print('~'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
    if soma % 2 == 0:
        print('Deu Par')
        print('~'*30)
        if escolha == 'P':
            print('Você Venceu')
            qtd_vitorias += 1
        else:
            print('Você Perdeu')
            break
        print('~'*30)
    else:
        print('Deu Ímpar')
        print('~'*30)
        if escolha == 'P':
            print('Você Perdeu')
            break
        else:
            print('Você Venceu')
            qtd_vitorias += 1
        print('Vamos jogar novamente...')
        print('~'*30)
print('~'*30)
print(f'GAME OVER. Você venceu {qtd_vitorias} vezes')