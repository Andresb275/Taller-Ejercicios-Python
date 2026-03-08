import pandas as pd
import codecs
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

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

    # Formatear texto en minúsculas
    return texto.strip().lower()

# Crear columna con profesión limpia
df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

# Corrección de errores residuales
correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}

# Aplicar correcciones
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# Función para limpiar y descifrar nombres
def limpiar_y_descifrar(texto):

    # Verificar valores nulos
    if pd.isna(texto):
        return texto

    # Eliminar caracteres especiales
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))

    # Quitar espacios
    texto = texto.strip()

    # Descifrar ROT13
    texto = codecs.decode(texto, 'rot_13')

    # Formatear nombre
    return texto.strip().title()

# Crear columna con nombres descifrados
df["nombre"] = df["nombre_cifrado"].apply(limpiar_y_descifrar)

# Filtrar Ana que sean medico
resultado = df[(df["nombre"] == "Ana") & (df["profesion_limpia"] == "medico")]

# Mostrar cantidad de registros
print(f"¿Cuántos registros tienen nombre 'Ana' y son 'Medico'?: {len(resultado)}")