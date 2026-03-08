import pandas as pd  # importar pandas
import re  # importar expresiones regulares

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# convertir a string
df["fecha_nacimiento_str"] = df["fecha_nacimiento"].astype(str).str.strip()
# convertir fecha a texto y quitar espacios

# patron para YYYY-MM-DD
patron = r'^\d{4}-\d{2}-\d{2}$'
# definir formato de fecha esperado

# detectar registros que no cumplen el patron
fechas_incorrectas = ~df["fecha_nacimiento_str"].str.match(patron)
# identificar fechas con formato diferente

# contar registros con formato diferente
cantidad_fechas_incorrectas = fechas_incorrectas.sum()
# contar fechas incorrectas

# resultado
print(f"Cantidad de registros con fecha de nacimiento con formato diferente a YYYY-MM-DD: {cantidad_fechas_incorrectas}")
# mostrar resultado