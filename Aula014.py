pessoasIdades = [['Isabeli', 15], ['Daniel', 16]]
print(pessoasIdades)
print(pessoasIdades[1])
print(pessoasIdades[0][1])
for i in pessoasIdades:
    print(i)
    
carro = []
dadosCarro = []
for i in range(0, 5):
    dadosCarro.append(str(input()))
    dadosCarro.append(int(input()))
    carro.append(dadosCarro[:])
    dadosCarro.clear()
for i in carro:
    if i[1] < 2015:
        print(i)
