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
- numpy
- matplotlib


# Forma de execução

No diretório principal, execute:

  `python scripts/data-processing.py`

