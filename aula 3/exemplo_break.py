

#lista de nomes
nomes = ['Giovana', 'Matheus', 'Goão', 'Pietro', 'Julia', 'Vitoria']

for indice, nome in enumerate(nomes):
    print(f'Estou no {indice} que possui o nome {nome}')
    if nome == 'Goão':
        nomes[indice] = 'João'
        break

print(nomes)