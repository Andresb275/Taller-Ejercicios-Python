import pandas as pd
import codecs

# Importa pandas para manejo de datos y codecs para descifrar ROT13

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Carga el archivo CSV en el DataFrame

# descifrar apellidos
df["apellido"] = df["apellido_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Descifra los apellidos codificados con ROT13

# limpiar datos
df["apellido"] = df["apellido"].str.strip().str.title()

# Elimina espacios y normaliza el formato del apellido

# encontrar el apellido mas frecuente
apellido_mas_frecuente = df["apellido"].value_counts().idxmax()

# Obtiene el apellido que más veces aparece

cantidad = df["apellido"].value_counts().max()

# Obtiene cuántas veces aparece ese apellido

print("Apellido más frecuente:", apellido_mas_frecuente)
print("Cantidad de veces:", cantidad)

# Muestra el resultado