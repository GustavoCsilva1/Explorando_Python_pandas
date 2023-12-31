# -*- coding: utf-8 -*-
"""explorando_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rjk9616brihIjkuX5VDyFxMpyqgeAM12
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)

pd.read_csv(url, sep=';')

dados = pd.read_csv(url, sep=';')
dados

dados.head(10)

dados[['Quartos', 'Valor']]

dados['Valor'].mean()

dados.groupby('Tipo').mean(numeric_only= True)

dados.groupby('Tipo')['Valor'].mean()

dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind= 'barh', figsize=(14, 10), color='purple');

dados.Tipo.unique()

imoveis_comerciais = ['Conjounto Comercial/Sala',
                      'Prédio Inteiro',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dados.query('@imoveis_comerciais in Tipo')

dados.query('@imoveis_comerciais not in Tipo')

df = dados.query('@imoveis_comerciais not in Tipo')
df.head()

df.Tipo.unique()

df.Tipo.value_counts(normalize = True)

df.Tipo.value_counts(normalize = True).to_frame().sort_values('Tipo')

df_percentual_tipo = df.Tipo.value_counts(normalize = True).to_frame().sort_values('Tipo')
df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color = 'green',
                        xlabel = 'Tipos', ylabel = 'Percentual')

df.query('Tipo == "Apartamento"')

df = df.query('Tipo == "Apartamento"')
df.head()

df.isnull()

df.isnull().sum()

df.fillna(0)

df = df.fillna(0)

df.isnull().sum()

df.query('Valor == 0 | Condominio == 0')

df.query('Valor == 0 | Condominio == 0').index

registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

df.drop(registros_a_remover, axis=0, inplace=True)

df.query('Valor == 0 | Condominio == 0')

df.head()

df.Tipo.unique()

df.drop('Tipo', axis=1, inplace=True)

df.head()

df['Quartos'] == 1

selecao1 = df['Quartos'] == 1
df[selecao1]

selecao2 = df['Valor'] < 1200
df[selecao2]

selecao_final = (selecao1) & (selecao2)
df[selecao_final]

df_1 = selecao_final = (selecao1) & (selecao2)

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df[selecao]

df2 = selecao = df[selecao]

df.to_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False)

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False, sep=';')

pd.read_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv', sep=';')

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
dados.head()

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados.head()

dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
dados.head()

dados['Descrição'] = dados['Tipo'] + ' em ' + dados['Bairro']
dados.head()

dados['Descrição'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' +  dados['Quartos'] + ' quartos ' +  ' e ' + dados['vagas'] + ' vagas(s) de garagem.'

dados['Descrição'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' +  dados['Quartos'].astype(str) + ' quartos ' +  ' e ' + dados['Vagas'].astype(str) + ' vagas(s) de garagem.'
dados.head()

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
dados.head()

dados.to_csv('dados_completos_dev.csv', index=False, sep=';')

