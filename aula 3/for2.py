#Estrutura de repetição For para listas
#Lista: estrutura de dados composta (armazena vários valores)

#cria uma lista de nome
nomes = ['Pietro', 'Ryan', 'maria', 'Gabriela', 'Sophia']

#imprime toda a lista (conjunto)
print(nomes)

#imprime um nome individualmente (Maria)
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

#inprime todos os nomes utilizados for - range
for i in range(5):
    print(nomes[1])

# outra opção para interar(percorrer de 1 em 1 ) sobre as listas
for nome in nomes:
    print(nome)
