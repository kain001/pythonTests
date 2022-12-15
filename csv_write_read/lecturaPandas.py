import pandas as pd
# SQL to pandas:
# https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#compare-with-sql

df = pd.read_csv('Book1.csv')
# imprimir resumen del dataframe:
# print(df)

# imprimir los primeros datos(se puede especificar cuales introduciendo el param):
# df.head()

# imprimir los ultimos registros del dataframe(se puede especificar cuales introduciendo el param):
# df.tail()

# resumen bastante completo(sum, unic, top , freq...):
# print(df.describe())

# filtrar el df por campo:
# df["example"]

# devolver un bool de coincidencias
# df["nombre"] == "michelo"

# salida de registros que cumplen los valores
# !importante -> operadores lógicos(| , &)
# df[df["fecha"] == "11/22/2022"]

# escribir el resultado de un dataframe filtrado en un csv
# df_filtered = df[df["fecha"] == "11/22/2022"]
# df_filtered.to_csv('test_etl')





