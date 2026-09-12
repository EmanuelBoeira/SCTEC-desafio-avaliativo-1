import sys
sys.path.append('./data/raw/')
sys.path.append('./data/processed/')
import pandas as pd

df_varejo = pd.read_csv('./data/raw/Base Varejo.csv', sep=';')

#------------------------------------
#initial analisys

#print(df_varejo.head())
#print(df_varejo.describe())
#print(df_varejo.info())
print('-'*50)

#after the previous inspection, it is possible see that are 3 empty collumns, so those columns will be removed
#this code separetes the columns from df_varejo that not contains 'Unnamed' on beginning 
df_varejo = df_varejo.loc[:, ~df_varejo.columns.str.contains('^Unnamed')]

print(df_varejo.info())
print('-'*50)

#text tratament
df_varejo['CL_GENERO'] = df_varejo['CL_GENERO'].str.strip().str.upper()
df_varejo['CL_SEG'] = df_varejo['CL_SEG'].str.strip().str.lower()
df_varejo['PR_CAT'] = df_varejo['PR_CAT'].str.strip().str.lower()
df_varejo['PR_NOME'] = df_varejo['PR_NOME'].str.strip().str.lower()

#converting object to datetime with pd.to_datetime()
df_varejo['DATA'] = pd.to_datetime(df_varejo['DATA'], dayfirst=True, format='mixed')

#duplicates tratament
print(f'Quantidade de duplicatas: {df_varejo.duplicated().sum()}')
#print(df_varejo[df_varejo.duplicated(keep=False)].sort_values(by=df_varejo.columns.tolist()))
print('-'*50)

#the quantite are being add in a new column called 'quantidade', so the number of logs duplicated will be pleced in 'quantidade' 
df_varejo = df_varejo.groupby(df_varejo.columns.tolist(), dropna=False).size().reset_index(name='quantidade')

#removing the duplicates
df_varejo.drop_duplicates(inplace=True)
print(f'Quantidade de duplicatas: {df_varejo.duplicated().sum()}')
print('-'*50)

#analisyng nulls(NaN or similar)

#print(df_varejo.groupby('PR_CAT')['PR_CAT'].count())        #tem #n/d
#print(df_varejo.groupby('CL_SEG')['CL_SEG'].count())
#print(df_varejo.groupby('PR_NOME')['PR_NOME'].count())      #tem #n/d
#print(df_varejo.groupby('CL_GENERO')['CL_GENERO'].count())

print(df_varejo.isnull().sum())
print('-'*50)

print(df_varejo.info())
print('-'*50)

#filling values NaN with 'desconhecido', to identify furter
if '#n/d' in df_varejo['PR_CAT'].values:
    df_varejo['PR_CAT'].replace('#n/d', 'desconhecido', inplace=True)
elif '#n/d' in df_varejo['PR_NOME'].values:
    df_varejo['PR_NOME'].replace('#n/d', 'desconhecido', inplace=True)

#creates a new csv with alterations
df_varejo.to_csv('./data/processed/varejo_processed.csv', index=False)

print(
'''
Resumo da análise inicial dos dados:
    - Colunas vazias foram removidas.

    - A coluna de CL_GENERO foi tratado com split() e upper().

    - Todas as outra colunas de texto foram tratadas com split() e lower().

    - As colunas numéricas já estão com valores numéricos.

    - Foi verificada a existência de 96.553 duplicatas.

    - A quantidade de duplicatas foi adicionada na última coluna 
      pois pode não ser um erro, já que o DataFrame é de um varejo.

    - As duplicatas foram removidas.

    - Não há existência de linhas com nulos NaN, mas existem valores #n/d
      que são entradas incorretas em PR_CAT e PR_NOME.

    - Os valores #n/d foram substituidos por NaN e depois por 'desconhecido'
'''
)
