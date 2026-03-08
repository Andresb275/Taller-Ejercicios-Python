import pandas as pd
import codecs
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Función para limpiar texto y descifrarlo con ROT13
def limpiar_y_descifrar(texto):

    # Verificar si el valor es nulo
    if pd.isna(texto):
        return texto

    # Eliminar caracteres especiales
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))

    # Quitar espacios
    texto = texto.strip()

    # Descifrar el texto usando ROT13
    texto = codecs.decode(texto, 'rot_13')

    # Formatear texto (primera letra en mayúscula)
    return texto.strip().title()

# Crear columna con nombres descifrados
df["nombre"] = df["nombre_cifrado"].apply(limpiar_y_descifrar)

# Crear columna con apellidos descifrados
df["apellido"] = df["apellido_cifrado"].apply(limpiar_y_descifrar)

# Filtrar registros donde nombre sea Jose y apellido Garcia
resultado = df[(df["nombre"] == "Jose") & (df["apellido"] == "Garcia")]

# Mostrar pregunta
print(f"Pregunta 30: ¿Cuántos registros tienen nombre 'Jose' y apellido 'Garcia'?")

# Mostrar cantidad de resultados encontrados
print(f"Respuesta 30: {len(resultado)}")