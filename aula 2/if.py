titulo =  input("Digite o nome do filme\n")
diarias = int(input('Por quantos dias alugou o filme\n'))
tempo = int(input("Por quantos dias ficou com o filme\n"))

valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

total = valor + multa

print ("total a pagar = ", total)