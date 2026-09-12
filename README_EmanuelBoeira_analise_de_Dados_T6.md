# Autor: Emanuel Boeira Martins

# Introdução

Este projeto foi executado como desafio avaliativo para o curso de Analise de Dados oferecido pelo SCTEC em parceria com o SENAI.
O projeto baseia-se na análise exploratória de dados(AED) de um arquivo .csv proveniente de um varejo. 
O arquivo .csv foi obtido pelo seguinte link: https://www.kaggle.com/datasets/namespaiva/base-varejo/data


# Sobre o projeto

  - O diretório data/ contém o arquivo .csv original, disponibilizado pelo link acima. 
  - O arquivo original está em data/raw.
  - O diretório data/processed/ contém um arquivo varejo_processed.csv que foi obtido após o processamento dos dados.
  - O diretório scripts/ contém os scripts usados durante o projeto.
  - O arquivo data-processing.py, disponível em scripts/, realiza o processamento inicial dos dados, como tratamento de nulos e correção de formatos, 
ao final da execução ele retorna uma breve descrição no terminal do que foi feito e gera o arquivo varejo_processed.csv.


# Dependências

- pandas
- matplotlib


# Forma de execução

No diretório principal, execute:

  `python scripts/data-processing.py` (para executar o tratamento dos dados)
  
  `python scripts/data-analysis.py` (para executar a análise dos dados)


# Sobre a análise

## Processamento dos dados

- Haviam 3 colunas vazias que form removidas.
- A coluna CL_GENERO foi tratada com spli() e upper().
- Todas as outras colunas de texto foram tratadas com split() e lower()
- As colunas numéricas já estavam com o tipo certo.
- Haviam 96.553 duplicatas.
- A quantidade de linhas duplicadas foi adicionada em uma nova coluna chamada 'quantidades'. Já que o DataFrame é de um varejo, foi escolhido esse método pois as linhas repetidas podem representar mais unidades de um mesmo pedido.
- Não há nulos identificados pelo pandas, mas haviam entradas com o valor #n/d nas colunas PR_CAT e PR_NOME.
- Esses valores inadequados foram substituidos por NaN e depois por 'desconhecido'.

## Análise dos dados
- A maior compra foi de 89 produtos.
- A maioria dos clientes não tem filho, isso é perceptível pela moda dessa informação.
- A média de filhos por cliente é de 1,14 filhos.
- Os 5 produtos mais vendidos são:
    - presunto cozido  (12.719 Un.)
    - sardinha         (6.610 Un.)
    - banana           (6.518 Un.)
    - escova de dente  (6.518 Un.)
    - gel              (6.517 Un.)
- O gênero feminino é o que apresenta mais compras.
- Ordem de segmentos com mais vendas:
    - b  (530.163 Un.)
    - c  (232.101 Un.)
    - a  (67.736 Un.)
- Ao analisar o gráfico de vendas ao longo do tempo:
    - Nos anos de 2020 a 2021 houve um aumento de vendas no final do ano, a partir do mês 10(outubro)
    - A partir de outubro de 2022 houve uma queda grande de vendas.
    - Seria importante analisar os momentos de pico isoladamente para determinar seu motivo, já que os dados presentes não expecificam uma correlação com as datas.
- Ao analisar o gráfico de vendas por categoria:
    - Alimentos é a categoria com mais vendas.
    - Acessórios é a categoria com menos vendas.


