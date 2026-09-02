# fatiamento
nomeInteiro = 'Isabeli Santos Silva'
print(nomeInteiro[0]) # vai imprimir apenas o valor dentro da variavel nomeInteiro na 15° posição
print(nomeInteiro[8:14]) # vai imprimi todos os valores dentro do intervalo de 8 - 14
print(nomeInteiro[15:20:2]) # vai imprimi todos os valores dentro do intervalo de 15 - 20 pulando de 2 em 2
print(nomeInteiro[:7]) # vai imprimir todos os valores até a setima casa
print(nomeInteiro[8:]) # vai imprimir todos os valores começando da oitava casa
print(nomeInteiro[8::3]) # vai imprimir todos os valores começando da oitava casa pulando de 3 em 3

# anâlise
print(len(nomeInteiro)) # conta quantos caracteres tem na string
print(nomeInteiro.count('a')) # vai contar quantas vezes um determinado caracter aparece, lembrando que tem diferença entre maiuscula ou minuscula
print(nomeInteiro.find('va')) # vai contar onde um determinado conjunto de caracteres aparece, lembrando que tem diferença entre maiuscula ou minuscula
print(nomeInteiro.find('princesa')) # quando não existir na string retorna o valor -1
print('Isabeli' in nomeInteiro) # verifica se existe aqueles caracteres e retorna True or False

# tranformação
print(nomeInteiro.replace('Silva', '- minha princesa')) # verifica se existe o conjunto de caracteres e modifica por outro conjunto de caracteres
print(nomeInteiro.upper()) # coloca toda a string em maiuscula
print(nomeInteiro.lower()) # coloca toda a string em minuscula
print(nomeInteiro.capitalize()) # deixa a string com a primeira letra da primeira palavra em maiuscula 
print(nomeInteiro.title()) # deixa a string com a primeira letra de todas as palavra em maiuscula 
print(nomeInteiro.strip()) # remove espaços inuteis
print(nomeInteiro.lstrip()) # remove espaços inuteis somente da esquerda
print(nomeInteiro.rstrip()) # remove espaços inuteis somente da direita

# divisão
print(nomeInteiro.split()) # divide a string pelos espaços em branco
print('-'.join(nomeInteiro)) # junta a string

