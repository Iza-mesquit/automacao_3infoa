#estrutura de repetição
#utilizadaa para repetir um conjunto de instruções por
#um número determinado de vezes (conhecidos)

# range -> comando utilizado para criar intervalos numéricos
#exemplo

#range(5) -> criar intervalos numéricos : 0, 1, 2, 3, 4
# (o último valor não entra no conjunto)

#range(valor inicial, valor final, passo)
#range(1, 5, 1) -> 1, 2, 3, 4
#range(4, 9, 2) -> 4, 6, 8
#range(5, 0, -1) -> 5, 4, 3, 2, 1


for valor in range(5):
    print(valor, end=" ")
print("\n")

for valor in range(1, 5, 1):
    print(valor, end=" ")
print("\n")

for valor in range(4, 9, 2):
    print(valor, end=" ")
print("\n")

for valor in range(5, 0, -1):
    print(valor, end=" ")
print("\n")

