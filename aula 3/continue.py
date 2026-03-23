#comando continue
#utilizado para interromper somente a interação
#do laço de repetição, continuando no inicio da proxima interação

#exemplo
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")

print("terminar o programa")