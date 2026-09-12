import sys
sys.path.append('./data/raw/')
sys.path.append('./data/processed/')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/processed/varejo_processed.csv', parse_dates=['DATA'])

#print(df['CL_FHL'].head())
print(df.info())
print('-' * 20)

#group by CO_ID and sum of sales
sales_sum_quantidade = df.groupby('CO_ID')['quantidade'].sum()
print('Top 5 maiores compras:\n')
print(sales_sum_quantidade.sort_values(ascending=False).head())
print('-' * 20)

#describe of CL_FHL(sons of clients)
describe_CL_FHL = df['CL_FHL'].describe()
describe_CL_FHL.loc['moda'] = df['CL_FHL'].mode().iloc[0]
print('Estatísticas de quantidade de filhos de clientes:\n')
print(describe_CL_FHL)
print('-' * 20)

#group by PR_ID, to get top 5 products sold
print('Top 5 produtos mais vendidos:\n')
print(df.groupby('PR_NOME')['PR_ID'].count().sort_values(ascending=False).head())
print('-' * 20)

#group by CL_GENERO, to get gender with more sales
print('Quantidade de vendas por gênero:\n')
print(df.groupby('CL_GENERO')['quantidade'].sum().sort_values(ascending=False))
print('-' * 20)

#group by CL_SEG, to get those with more sales
print('Segmentos com mais vendas:\n')
print(df.groupby('CL_SEG')['quantidade'].sum().sort_values(ascending=False))
print('-' * 20)

#plot of sales in time and sales by category
fig, ax = plt.subplots(1,2)

sales = df.groupby(df['DATA'].dt.to_period('M'))['quantidade'].sum()
sales.index = sales.index.to_timestamp()

quant_by_category = df.groupby('PR_CAT')['quantidade'].sum().sort_values(ascending=False)

ax[0].plot(sales)
ax[0].set_xlabel('Ano - Mês')
ax[0].set_ylabel('Vendas(Un.)')
ax[0].set_title('Quantidade de vendas por mês.')

ax[1].bar(quant_by_category.index, quant_by_category, 0.4)
ax[1].set_title('Quantidade total de vendas por categoria.')

plt.show()

print(
    '''
    OBS.: A coluna DATA havia sido convertida para datetime
    no script anterior, mas essa alteração não foi repassada
    para esse código. Isso ocorre porque o arquivo CSV não
    armazena os tipos das colunas, o pandas é quem faz isso.

    - A primeira tabela mostra os 5 compradores
    com maiores compras pelo ID.

    - A segunda seção mostra estatísticas das quantidades
    de filhos por cliente.

    - A terceira seção mostra o 5 produtos mais vendidos.
        1º - presunto cozido
        2º - sardinha
        3º - banana
        4º - escova de dente
        5º - gel

    - A quarta seção mostra a quantidade de compras por gênero:
        Feminino:  432.576 compras
        Masculino: 397.424 compras

    - A quinta seção mostra a quantidade de compras por segmento:
        a:  67.736
        b: 530.163
        c: 232.101

    - Análise do gráfico de vendas ao longo do tempo:
        - Nos anos de 2020 2021 houve um aumento de vendas no final
        do ano, a partir do mês 10 (outubro).
        - A partir de outubro de 2022 houve uma queda brusca de vendas.
        - Seria importante analisar os momentos de picos para determinar
        seu motivo, já que não há relação direta nos os dados fornecidos.

    - Análise do gráfico de vendas por categoria:
        - Alimentos é a categoria com maiores vendas.
        - Acessórios é a categoria com menores vendas.
    '''
)
