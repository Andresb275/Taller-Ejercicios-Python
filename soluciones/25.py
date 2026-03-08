import pandas as pd
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

# Convertir salario a texto
df["salario_str"] = df["salario"].astype(str)

# Diccionario de correcciones de caracteres
reemplazos_salario = {
    "l": "1",
    "O": "0",
    "e": "3",
    "aprox.": ""
}

# Reemplazar caracteres incorrectos en salario
for old, new in reemplazos_salario.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)

# Cambiar coma por punto
df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)

# Eliminar caracteres no numéricos
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)

# Convertir salario a número
df["salario_limpio"] = pd.to_numeric(df["salario_limpio"], errors='coerce')

# Filtrar abogados con salario mayor a 10,000,000
resultado = df[(df["profesion_limpia"] == "abogado") & (df["salario_limpio"] > 10000000)]

# Mostrar cantidad de registros
print(f"¿Cuántos registros tienen profesión 'Abogado' y salario > 10,000,000?: {len(resultado)}")