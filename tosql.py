import pandas as pd
# import dataframe gastos
df = pd.read_excel("C:/Users/julio/OneDrive/Documentos/codes/vidhya/gastosPY.xlsx")
#list columns
print(df.columns)
# %%
from collections import defaultdict
# adiciona o id na coluna apropriada
# cria um dataframe apenas para o destino e o id
account_df = df[["id_account", "account"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário o len(temp)+1 para o primeiro id ser 1.
temp = defaultdict(lambda: len(temp)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
account_df["id_account"] = [temp[ele] for ele in account_df["account"]]
# aplica o id na coluna do dataframe original
df["id_account"] = account_df['id_account']
# apaga os valores nulos para o print de insert into
account_df = account_df.dropna().drop_duplicates()
# loop com o print dos resultados formatados para sql
print("INSERT INTO account\n\t\tVALUES", end=" ")
for i in account_df.index:
    print("(", account_df["id_account"][i],", '", account_df["account"][i], sep= "", end="'),\n\t\t")
# %%
# cria um dataframe apenas para o tipo de compra e o id
buytype_df = df[["id_buytype", "buytype"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp1 = defaultdict(lambda: len(temp1)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
buytype_df["id_buytype"] = [temp1[ele] for ele in buytype_df["buytype"]]
# aplica o id na coluna do dataframe original
df["id_buytype"] = buytype_df['id_buytype']
# apaga os valores nulos e duplicados
buytype_df = buytype_df.dropna().drop_duplicates()
# loop com o print dos resultados formatados para sql
print("INSERT INTO buytype\n\t\tVALUES", end=" ")
for i in buytype_df.index:
    print("(", df["id_buytype"][i],", '", df["buytype"][i], sep= "", end="'),\n\t\t")
# %%
# cria um dataframe apenas para o tipo de compra e o id
installment_df = df[["id_installment", "installment"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp2 = defaultdict(lambda: len(temp2)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
installment_df["id_installment"] = [temp2[ele] for ele in installment_df["installment"]]
# aplica o id na coluna do dataframe original
df["id_installment"] = installment_df['id_installment']
# apaga os valores nulos e duplicados
installment_df = installment_df.dropna().drop_duplicates()
# loop com o print dos resultados formatados para sql
print("INSERT INTO installment\n\t\tVALUES", end=" ")
for i in installment_df.index:
    print("(", df["id_installment"][i],", '", df["installment"][i], sep= "", end="'),\n\t\t")
# %%
# cria um dataframe apenas para a categoria e o id
category_df = df[["id_category", "category"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp3 = defaultdict(lambda: len(temp3)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
category_df["id_category"] = [temp3[ele] for ele in category_df["category"]]
# aplica o id na coluna do dataframe original
df["id_category"] = category_df['id_category']
# apaga os valores nulos e duplicados
category_df = category_df.dropna().drop_duplicates()
# loop com o print dos resultados formatados para sql
print("INSERT INTO category\n\t\tVALUES", end=" ")
for i in category_df.index:
    print("(", df["id_category"][i],", '", df["category"][i], sep= "", end="'),\n\t\t")
# %%
# adiciona o id na coluna apropriada
# cria um dataframe apenas para o destino e o id
destination_df = df[["destination", "id_destination"]]
# cria uma variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp4 = defaultdict(lambda: len(temp4)+1)
# loop adicionando os ids conforme o elemento na coluna de destino
destination_df["id_destination"] = [temp4[ele] for ele in destination_df["destination"]]
# aplica o id na coluna do dataframe original
df['id_destination'] = destination_df['id_destination']
# apaga os valores nulos e duplicados
destination_df = destination_df.dropna().drop_duplicates()
# loop com o print dos resultados formatados para sql
print("INSERT INTO destination\n\t\tVALUES", end=" ")
for i in destination_df.index:
    print("(", df["id_destination"][i],", '", df["destination"][i], sep= "", end="'),\n\t\t")
# %%
# adiciona o id na coluna apropriada
# cria um dataframe apenas para o produto e o id
product_df = df[["product", "id_product"]]
# cria outra variável com a função defaultdict, para a criação das ids. É necessário outra variável temp para que o id não seja a continuação do anterior.
temp5 = defaultdict(lambda: len(temp5)+1)
# loop adicionando os ids conforme o elemento na coluna de produto
product_df["id_product"] = [temp5[ele] for ele in product_df["product"]]
# aplica o id na coluna do dataframe original
df["id_product"] = product_df["id_product"]
# apaga os valores nulos e duplicados
product_df = product_df.dropna().drop_duplicates()
# loop com o print dos resultados para conferência
print("INSERT INTO product\n\t\tVALUES", end=" ")
for i in product_df.index:
    print("(", product_df["id_product"][i],", '", product_df["product"][i], sep= "", end="'),\n\t\t")
# %%

# também é possível utilizar os seguintes comandos para criar 
# um arquivo csv dos dataframes individuais e conferir os resultados:

# productFrame = pd.DataFrame.from_dict(product_df)
# productFrame.to_csv('product_df.csv', index = False)

# %%
# adiciona o id na coluna apropriada
df["id"] = df.index+1

# print final
print("INSERT INTO operation\n\t\tVALUES ", end=" ")
for i in df.index:
    print("(", df["id"][i],", '", df["date"][i], "', ", df["price"][i], ", ", df["installment"][i], ", ",df["id_product"][i], ", ", df["id_category"][i], ", ", df["id_destination"][i], ", ", df["id_buytype"][i], ", ", df["id_account"][i], sep= "", end="),\n\t\t")

# %%
