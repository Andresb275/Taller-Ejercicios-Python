import pandas as pd
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Diccionario para corregir ciudades con caracteres alterados
correcciones_ciudades = {
    "S@nt@ M@rt@": "Santa Marta", "V@ll3dup@r": "Valledupar",
    "M@niz@l3s": "Manizales", "Sinc3l3jo": "Sincelejo",
    "Buc@r@m@ng@": "Bucaramanga", "Tunj@": "Tunja",
    "Ib@gu3": "Ibague", "C@rt@g3n@": "Cartagena",
    "Arm3ni@": "Armenia", "M3d3llin": "Medellin",
    "Cucut@": "Cucuta", "C@li": "Cali",
    "P3r3ir@": "Pereira", "Mont3ri@": "Monteria",
    "Bogot@": "Bogota", "Vill@vic3ncio": "Villavicencio",
    "N3iv@": "Neiva", "Pop@y@n": "Popayan",
    "B@rr@nquill@": "Barranquilla", "P@sto": "Pasto"
}

# Limpiar espacios en ciudades
df["ciudad"] = df["ciudad"].str.strip()

# Corregir nombres de ciudades
df["ciudad"] = df["ciudad"].replace(correcciones_ciudades)

# Eliminar caracteres especiales
df["ciudad"] = df["ciudad"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)

# Formatear ciudades (primera letra en mayúscula)
df["ciudad"] = df["ciudad"].str.strip().str.title()

# Función para limpiar la profesión
def limpiar_profesion(texto):

    # Verificar valores nulos
    if pd.isna(texto):
        return texto

    # Quitar espacios
    texto = str(texto).strip()

    # Reemplazar 3 por e entre letras
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)

    # Reemplazar @ por a entre letras
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)

    # Eliminar caracteres no válidos
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)

    # Convertir a minúsculas
    return texto.strip().lower()

# Crear columna con profesión limpia
df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

# Correcciones finales de profesión
correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}

# Aplicar correcciones
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# Filtrar registros donde la profesión sea ingeniero
ingenieros = df[df["profesion_limpia"] == "ingeniero"]

# Obtener la ciudad con más ingenieros
ciudad_top = ingenieros["ciudad"].value_counts().idxmax()

# Obtener la cantidad de ingenieros en esa ciudad
cantidad = ingenieros["ciudad"].value_counts().max()

# Mostrar resultado
print(f"¿Cuál es la ciudad con más 'Ingenieros'?: {ciudad_top} con {cantidad} ingenieros")