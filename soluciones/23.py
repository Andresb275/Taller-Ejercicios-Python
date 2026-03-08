import pandas as pd
import codecs
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Diccionario de corrección de ciudades
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

# Formatear texto de ciudades
df["ciudad"] = df["ciudad"].str.strip().str.title()

# Función para limpiar y descifrar nombres
def limpiar_y_descifrar(texto):

    # Verificar valores nulos
    if pd.isna(texto):
        return texto

    # Quitar caracteres especiales
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))

    # Quitar espacios
    texto = texto.strip()

    # Descifrar ROT13
    texto = codecs.decode(texto, 'rot_13')

    # Formatear nombre
    return texto.strip().title()

# Crear columna con nombres descifrados
df["nombre"] = df["nombre_cifrado"].apply(limpiar_y_descifrar)

# Filtrar Carlos en Cali
resultado = df[(df["nombre"] == "Carlos") & (df["ciudad"] == "Cali")]

# Mostrar cantidad de registros
print(f"¿Cuántos registros tienen nombre Carlos y viven en Cali?: {len(resultado)}")