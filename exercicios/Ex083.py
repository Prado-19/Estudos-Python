expressao = str(input('Digite a expressão: '))
lista = []
for i in expressao:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
