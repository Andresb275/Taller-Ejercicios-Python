# Importar la librería pandas para trabajar con el dataset
import pandas as pd

# Cargar el dataset desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# Detectar emails que tengan espacios al inicio o al final
# Se convierte la columna a texto y se usa una expresión regular para buscar esos espacios
emails_con_espacios = df["email"].astype(str).str.match(r'^\s+|\s+$')

# Contar cuántos registros cumplen esa condición
cantidad_emails_con_espacios = emails_con_espacios.sum()

# Mostrar el resultado final
print("Registros con email que tiene espacios adicionales:", cantidad_emails_con_espacios)