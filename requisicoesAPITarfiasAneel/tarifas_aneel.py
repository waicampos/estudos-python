'''
Referências:
    SQL: https://www.w3schools.com/sql/default.asp
    lib requests: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
'''


import requests
import pandas as pd

# Exemplo1: Filtrando os dados da consulta-----------
query = """
    SELECT *
    FROM "fcf2906c-7c32-4b9b-a637-054e7a5234f4"
    WHERE "SigAgente"='CELESC' AND
          "DscModalidadeTarifaria"='Azul' AND
          "DscSubGrupo"='A4' AND
          "DscModalidadeTarifaria"='Azul' AND
          "DatInicioVigencia" > '2023-03-15'
"""
r = requests.get(f'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql?sql={query}')
print(r.json())
df = pd.DataFrame(r.json()['result']['records'])
print("Exemplo1: Filtrando os dados da consulta-----------")
print(df.loc[:, ['SigAgente','NumCNPJDistribuidora', 'DatInicioVigencia', 'DatFimVigencia', 'DatGeracaoConjuntoDados','VlrTUSD', 'VlrTE']])
print("-----------Exemplo1: Filtrando os dados da consulta")

# Exemplo2: Consultando nome das distribuidoras-----------
query2 = """
    SELECT DISTINCT "SigAgente"
    FROM "fcf2906c-7c32-4b9b-a637-054e7a5234f4"
"""
r = requests.get(f'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql?sql={query2}')
ans = r.json()['result']['records']
lista_distribuidoras = [x['SigAgente'] for x in ans]
print("Exemplo2: Consultando nome das distribuidoras-----------")
print(lista_distribuidoras)
print("Exemplo2: Consultando nome das distribuidoras-----------")
