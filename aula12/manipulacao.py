'''
1)Carregue o arquivo Excel chamado notas_estudantes.xlsx da seguinte forma:
Armazene os dados da aba "Notas" em um DataFrame chamado df_notas.
Armaze-ne os dados da aba "Atividades" em um DataFrame chamado df_atividades.
'''

import pandas as pd
tabela = pd.read_excel("aula12\\notas_estudantes.xlsx", sheet_name="Notas")

'''
Adicione um novo registro ao DataFrame df_notas com os seguintes dados:
Nome: 'Lucas Silva'
Atividade: 'Prova Final'
Nota: 8.5
'''

tabela.loc[len(tabela)] = ['Lucas Silva','Prova Final',8.5]
print(tabela)

'''
3. Atualização de Dados
No DataFrame df_notas, atualize para 9.0 a nota da atividade 'Trabalho 1' da estudante 'Ana Souza'.
'''