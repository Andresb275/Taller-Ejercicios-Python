import pandas as pd
import codecs

# Importa pandas para manejar datos y codecs para el descifrado ROT13

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Carga el archivo CSV en un DataFrame

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Descifra los nombres codificados con ROT13
# y los guarda en la columna "nombre"

# limpiar y normalizar
df["nombre"] = df["nombre"].str.strip().str.title()

# Elimina espacios y normaliza el formato del nombre

# contar "Juan"
cantidad_juan = (df["nombre"] == "Juan").sum()

# Cuenta cuántos registros tienen el nombre "Juan"

print("Cantidad de personas llamadas Juan:", cantidad_juan)

# Muestra el resultado

