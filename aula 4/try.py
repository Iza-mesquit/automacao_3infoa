
#Crie um script que solicita que o usuário digite dois numeros
#inteiros. Após o programa deve realizar a divisão do prrimeiro número pelo segundo.
#por fim deve mostrar o resuktado da divisão

while True:
    try:
        n1 = int(input(("Digite um número \n")))
        n2 = int(input(("Digite outro número \n")))
        resultado = n1/n2
        print ("A divisão de ",n1," por ",n2," é ",resultado)
        break
    except ValueError:
        print('o valor digitado é inválido, tente novamente')
    except ZeroDivisionError:
        print('Não é possível dividir por 0, tente novamente')
    except Exception as bolinha:
        print('Ocorreu um erro: ', bolinha)