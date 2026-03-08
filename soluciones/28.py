import pandas as pd
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Función para limpiar la profesión
def limpiar_profesion(texto):

    # Verificar si el valor es nulo
    if pd.isna(texto):
        return texto

    # Quitar espacios al inicio y final
    texto = str(texto).strip()

    # Reemplazar 3 por e cuando está entre letras
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)

    # Reemplazar @ por a cuando está entre letras
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)

    # Eliminar caracteres que no sean letras o espacios
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)

    # Convertir a minúsculas y eliminar espacios
    return texto.strip().lower()

# Crear nueva columna con profesión limpia
df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

# Correcciones finales de profesiones mal escritas
correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}

# Aplicar correcciones
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# Convertir salario a texto para poder limpiarlo
df["salario_str"] = df["salario"].astype(str)

# Diccionario para corregir caracteres en salario
reemplazos_salario = {
    "l": "1",
    "O": "0",
    "e": "3",
    "aprox.": ""
}

# Reemplazar caracteres incorrectos en el salario
for old, new in reemplazos_salario.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)

# Reemplazar comas por puntos
df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)

# Eliminar caracteres que no sean números o punto
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)

# Convertir salario limpio a número
df["salario_limpio"] = pd.to_numeric(df["salario_limpio"], errors='coerce')

# Calcular salario promedio por profesión
promedio_por_profesion = df.groupby("profesion_limpia")["salario_limpio"].mean()

# Obtener profesión con mayor salario promedio
profesion_top = promedio_por_profesion.idxmax()

# Obtener el valor del salario promedio más alto
salario_top = promedio_por_profesion.max()

# Mostrar resultado
print(f"¿Cuál es la profesión con el salario promedio más alto?:{profesion_top.title()} con un promedio de ${salario_top:,.0f}")