#Pandas - Biblioteca de Manipulação de Dados Tabulares(Planilha)

#Manipulação de dados (inserir, atualizar, excluir e consultar)


# instalar a lib: pip install pandas

#uso
import pandas as pd

#criar a quadro de dados (Dataframe) equivalente a tabela no DB
# cria a variável planilha que vai armazenar a planilha do excel
#que foi lida pelo pandas
planilha = pd.read_excel('aula10\\Planilha.xlsx')

#visualizar planilha
print(planilha)

#inserir um registro na planilha
planilha.loc[len(planilha)] = ['Ivan', 40,'M',85,1.75]
print(planilha)

#inserir um registro na planilha
planilha.loc[len(planilha)] = ['izabel vitoria',17,'F',82,1.85]
print(planilha)

#atualizar a linha inteira
planilha.loc[19] = ['Ivan', 40,'M',85,1.75]
print(planilha)

#remove um registro da planilha
print("Removeu o IVAN")
planilha_sem_ivan = planilha.drop(19)
print(planilha_sem_ivan)
print("O ivan ainda esta aqui")
planilhha = planilha_sem_ivan
print(planilha)

#remove um regitro da planilha
planilha planilha.drop(19)
#ou
planilha.drop(19, inplace=True)

print("A planilha tem", len(planilha), "linhas")