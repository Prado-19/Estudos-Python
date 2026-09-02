larguraDaParede = float(input('Qual a largura da parede: '))
alturaDaParede = float(input('Qual a altura da parede: '))
areaDaParede = larguraDaParede * alturaDaParede
quantidadeDeTintaParaPintarParede = areaDaParede / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². Para pintar essa parede, você precisará de {}l de tinta.'.format(larguraDaParede, alturaDaParede, areaDaParede, quantidadeDeTintaParaPintarParede))