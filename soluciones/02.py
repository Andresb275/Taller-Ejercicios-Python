import pandas as pd
import codecs

# Importa pandas para manejar el dataset
# Importa codecs para aplicar el descifrado ROT13

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Lee el archivo CSV y lo guarda en el DataFrame df

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Aplica el descifrado ROT13 a la columna "nombre_cifrado"
# y guarda el resultado en una nueva columna llamada "nombre"

# contar cuantas veces aparece Maria
cantidad_maria = (df["nombre"].str.strip().str.title() == "Maria").sum()

# Limpia los nombres:
# strip() elimina espacios
# title() normaliza el formato (Maria, no MARIA o maria)
# Luego cuenta cuántos son exactamente "Maria"

print("Cantidad de personas llamadas Maria:", cantidad_maria)

# Muestra el total encontrado