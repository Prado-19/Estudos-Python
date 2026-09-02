import random
aluno01 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input('Terceiro aluno: ')
aluno04 = input('Quarto aluno: ')
listaAlunos = [aluno01, aluno02, aluno03, aluno04]
alunoSorteado = random.choice(listaAlunos)
print('O aluno sorteado foi {}'.format(alunoSorteado))