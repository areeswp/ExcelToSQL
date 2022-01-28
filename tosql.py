import pandas as pd
import numpy as np
# import dataframe gastos
df = pd.read_excel("git\ExcelToSQL\gastosPY.xlsx")
#lista as colunas
print(df.columns)
# %%
from collections import defaultdict
# cria uma coluna de id, se não existir
try:
    df.insert(5, "id_account", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
# cria uma variável com a função defaultdict, para a criação das ids. É necessário o len(temp)+1 para o primeiro id ser 1.
temp = defaultdict(lambda: len(temp)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
df["id_account"] = [temp[ele] for ele in df["account"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
account_df = df[['id_account', 'account']].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO account\n\t\tVALUES", end=" ")
for i in account_df.index:
    print("(", account_df["id_account"][i],", '", df["account"][i], sep= "", end="'),\n\t\t")
print (";")
# %%
# cria uma coluna de id, se não existir
try:
    df.insert(3, "id_buytype", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
#buytype_df = df[["id_buytype", "buytype"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp1 = defaultdict(lambda: len(temp1)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
df["id_buytype"] = [temp1[ele] for ele in df["buytype"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
buytype_df = df[["id_buytype", "buytype"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO buytype\n\t\tVALUES", end=" ")
for i in buytype_df.index:
    print("(", df["id_buytype"][i],", '", df["buytype"][i], sep= "", end="'),\n\t\t")
print (";")
    
# %%
# cria uma coluna de id, se não existir
try:
    df.insert(1, "id_category", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp3 = defaultdict(lambda: len(temp3)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
df["id_category"] = [temp3[ele] for ele in df["category"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
category_df = df[["id_category", "category"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO category\n\t\tVALUES", end=" ")
for i in category_df.index:
    print("(", df["id_category"][i],", '", df["category"][i], sep= "", end="'),\n\t\t")
print (";")
# %%
# cria uma coluna de id, se não existir
try:
    df.insert(6, "id_destination", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp4 = defaultdict(lambda: len(temp4)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
df["id_destination"] = [temp4[ele] for ele in df["destination"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
destination_df = df[["id_destination", "destination"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO destination\n\t\tVALUES", end=" ")
for i in destination_df.index:
    print("(", df["id_destination"][i],", '", df["destination"][i], sep= "", end="'),\n\t\t")
print (";")
# %%
try:
    df.insert(3, "id_product", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
# cria outra variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp5 = defaultdict(lambda: len(temp5)+1)
# loop adicionando os ids conforme o elemento na coluna de produto
df["id_product"] = [temp5[ele] for ele in df["product"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
product_df = df[["id_product", "product"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO product\n\t\tVALUES", end=" ")
for i in product_df.index:
    print("(", product_df["id_product"][i],", '", product_df["product"][i], sep= "", end="'),\n\t\t")
print (";")
# %%

# também é possível utilizar os seguintes comandos para criar 
# um arquivo csv dos dataframes individuais e conferir os resultados:

# productFrame = pd.DataFrame.from_dict(product_df)
# productFrame.to_csv('product_df.csv', index = False)

# %%
# cria uma coluna de id, se não existir, e a preenche
try: 
    df.insert(0, "id", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
df["id"] = df.index+1
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO operation\n\t\tVALUES ", end=" ")
for i in df.index:
    print("(", df["id"][i],", '", df["date"][i], "', ", df["price"][i], ", ", df["installment"][i], ", ",df["id_product"][i], ", ", df["id_category"][i], ", ", df["id_destination"][i], ", ", df["id_buytype"][i], ", ", df["id_account"][i], sep= "", end="),\n\t\t")
print (";")
# %%

# para exportar o excel final:
# df.to_excel("dataframeGastos.xlsx", index = False)