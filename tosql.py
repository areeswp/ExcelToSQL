import pandas as pd
import numpy as np
# import dataframe gastos
df = pd.read_excel("git\ExcelToSQL\gastosPY.xlsx")
#list columns
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
df["id_account"] = [temp[ele] for ele in df["accounts"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
account_df = df[['id_account', 'accounts']].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO accounts\n\t\tVALUES", end=" ")
for i in account_df.index:
    print("(", account_df["id_account"][i],", '", df["accounts"][i], sep= "", end="'),\n\t\t")
print (";")
# %%
# cria uma coluna de id, se não existir
try:
    df.insert(3, "id_buytypes", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
#buytype_df = df[["id_buytype", "buytype"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp1 = defaultdict(lambda: len(temp1)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
df["id_buytype"] = [temp1[ele] for ele in df["buytypes"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
buytype_df = df[["id_buytype", "buytypes"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO buytypes\n\t\tVALUES", end=" ")
for i in buytype_df.index:
    print("(", df["id_buytype"][i],", '", df["buytypes"][i], sep= "", end="'),\n\t\t")
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
df["id_category"] = [temp3[ele] for ele in df["categories"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
categories_df = df[["id_category", "categories"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO categories\n\t\tVALUES", end=" ")
for i in categories_df.index:
    print("(", df["id_category"][i],", '", df["categories"][i], sep= "", end="'),\n\t\t")
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
df["id_destination"] = [temp4[ele] for ele in df["destinations"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
destinations_df = df[["id_destination", "destinations"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO destinations\n\t\tVALUES", end=" ")
for i in destinations_df.index:
    print("(", df["id_destination"][i],", '", df["destinations"][i], sep= "", end="'),\n\t\t")
print (";")
# cria uma coluna de id, se não existir
try:
    df.insert(3, "id_product", np.nan) # o primeiro argumento da função é o número da coluna onde vai ser inserida
except:
    pass
# cria outra variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp5 = defaultdict(lambda: len(temp5)+1)
# loop adicionando os ids conforme o elemento na coluna de produto
df["id_product"] = [temp5[ele] for ele in df["products"]]
# passa os valores únicos de id para outro dataframe (sem valores nulos nem duplicados)
products_df = df[["id_product", "products"]].dropna().drop_duplicates()
# formatação PostgreSQL e loop com o print dos resultados para conferência
print("INSERT INTO products\n\t\tVALUES", end=" ")
for i in products_df.index:
    print("(", products_df["id_product"][i],", '", products_df["products"][i], sep= "", end="'),\n\t\t")
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
print("INSERT INTO operations\n\t\tVALUES ", end=" ")
for i in df.index:
    print("(", df["id"][i],", '", df["date"][i], "', ", df["price"][i], ", ", df["installments"][i], ", ",df["id_product"][i], ", ", df["id_category"][i], ", ", df["id_destination"][i], ", ", df["id_buytype"][i], ", ", df["id_account"][i], sep= "", end="),\n\t\t")
print (";")
# %%
# para exportar o excel final:
# df.to_excel("dataframeGastos.xlsx", index = False)
