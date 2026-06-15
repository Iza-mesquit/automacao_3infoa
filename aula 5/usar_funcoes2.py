from aula4.funcao import imprimir
from aula4.funcao import ler, pulaLinha, somar

#usando as funções
imprimir('Digite o número 1')
nu1 = ler()
pulaLinha()
pulaLinha()

imprimir('Digite o número 2')
nu2  = ler()

resposta = somar(nu1, nu2)
imprimir(f'O resultado é {resposta}')