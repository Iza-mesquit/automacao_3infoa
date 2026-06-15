import aula4.funcao as ivan

#usando as funções
ivan.imprimir('Digite o número 1')
nu1 = ivan.ler()
ivan.pulaLinha()
ivan.pulaLinha()

ivan.imprimir('Digite o número 2')
nu2  = ivan.ler()

resposta = ivan.somar(nu1, nu2)
ivan.imprimir(f'O resultado é {resposta}')