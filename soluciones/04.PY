import pandas as pd
import codecs

# Importa pandas para manejo de datos y codecs para aplicar ROT13

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Carga el archivo CSV en el DataFrame

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Descifra los nombres codificados con ROT13

# limpiar y normalizar
df["nombre"] = df["nombre"].str.strip().str.title()

# Elimina espacios y normaliza el formato del nombre

# obtener nombre mas frecuente
nombre_mas_frecuente = df["nombre"].value_counts().idxmax()

# Obtiene el nombre que más veces aparece

cantidad = df["nombre"].value_counts().max()

# Obtiene cuántas veces aparece ese nombre

print("Nombre más frecuente:", nombre_mas_frecuente)
print("Cantidad de veces:", cantidad)

# Muestra el resultado