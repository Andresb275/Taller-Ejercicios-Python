import pandas as pd

# Importa la librería para manejo de datos

df = pd.read_csv("data/personas.csv")

# Carga el archivo CSV en un DataFrame

ids_no_numericos = df["id"].astype(str).str.contains(r"\D")

# Busca IDs que contengan caracteres no numéricos (\D)

cantidad = ids_no_numericos.sum()

# Cuenta cuántos registros cumplen la condición

print("Filas con id no numérico:", cantidad)

# Muestra el total encontrado


