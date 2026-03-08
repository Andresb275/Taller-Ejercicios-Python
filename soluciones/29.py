import pandas as pd
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Función para limpiar el email
def limpiar_email(texto):

    # Verificar si el valor es nulo
    if pd.isna(texto):
        return texto

    # Convertir a texto y quitar espacios
    texto = str(texto).strip()

    # Convertir todo a minúsculas
    texto = texto.lower()

    # Eliminar prefijo "mailto:"
    texto = re.sub(r'^mailto:', '', texto)

    # Eliminar caracteres como (), <>
    texto = re.sub(r'[()<>]', '', texto)

    # Quitar espacios alrededor del @
    texto = re.sub(r'\s*@\s*', '@', texto)

    # Quitar espacios alrededor del punto
    texto = re.sub(r'\s*\.\s*', '.', texto)

    # Corregir dominio mal escrito
    texto = re.sub(r'@mail\.com$', '@gmail.com', texto)

    # Eliminar espacios finales
    return texto.strip()

# Crear nueva columna con el email limpio
df["email_limpio"] = df["email"].apply(limpiar_email)

# Contar emails que terminan en @gmail.com
cantidad = df["email_limpio"].str.endswith("@gmail.com").sum()

# Mostrar resultado
print(f"¿Cuántos registros tienen email con dominio 'gmail.com'?: {cantidad}")