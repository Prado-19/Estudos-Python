times_classificacao = (
    "Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Red Bull Bragantino",
    "Bahia", "Coritiba", "São Paulo", "Atlético-MG", "Corinthians",
    "Cruzeiro", "Botafogo", "Vitória", "Internacional", "Santos",
    "Grêmio", "Vasco da Gama", "Remo", "Mirassol", "Chapecoense"
)


print('{: ^100}'.format('TABELA DO BRASILEIRÂO NA PARADA PARA A COPA'))
print('=-'*50)
print(f'Os 4 primeiros são {times_classificacao[:4]}')
print('=-'*50)
print(f'Os 4 últimos são {times_classificacao[16:]}')
print('=-'*50)
print('{: ^100}'.format('Os times em ordem alfabética são'))
times_ordem_alfabetica = sorted(times_classificacao)
for i in times_ordem_alfabetica:
    print(i)
print('=-'*50)
print('{: ^100}'.format('Classificação Completa'))
for i in times_classificacao:
    print(i)
    
