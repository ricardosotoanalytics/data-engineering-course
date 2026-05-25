import pandas as pd
archivo = "data/empleados.xlsx"
df = pd.read_excel(archivo, engine="openpyxl")
print(df.head())

