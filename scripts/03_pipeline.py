import pandas as pd

### EXTRAER
df = pd.read_excel("data/empleados.xlsx")


### TRANSFORMAR
# eliminar filas
df = df.dropna()

# nombres en mayúsculas
df["nombre"] = df["nombre"].str.upper()

# Crear columna "Bono"
df["bono"] = df["salario"]*0.10

# Filtrar informacion
# ventas = df[df["area"] == "Ventas"]


### CARGAR
# Guardar resultados
df.to_csv("output/reportefinal.csv", index = False)


# dataframe final
print("Pipeline ejecutado correctamente")



