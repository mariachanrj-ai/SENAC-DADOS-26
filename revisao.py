import pandas as pd
dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin1',sep=';') 
# print(df)   #le todas as linhas - lento
# print(df.head())  #imprime as 5 primeiras linhas
# print(df.head(10))   #lê somente as 10 primeiras linhas
# print(df.tail(10))   #imprime as últimas 10 linhas
# print(df.columns) #imprime colunas
#agrupamento de dados - somar dados qualitativos totais - ex - total de furto celular por delegacia
df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()  # dados qualitativos entre parenteses e quantitativos entre colchetes .FunçãoMatemática()
print(df_furto_celular_cisp) #sem índice, gera uma série; com .reset_index() gera dataframe