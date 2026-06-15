#estrutura de repetição: while

while True:
    usuario = input('Digite seu login\n')
    senha = input('Digite sua senha:\n')

    if(usuario == 'admin' and senha=='123'):
        break
    else:
        print('Falha ao realizar o login')

print('Bem vindo ao sistema')