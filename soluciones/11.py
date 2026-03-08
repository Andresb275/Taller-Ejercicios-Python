# 1. Importar las librerías necesarias para el análisis de datos y uso de expresiones regulares
import pandas as pd
import re

# 2. Cargar el dataset desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# 3. Función para limpiar y normalizar los nombres de profesiones
def limpiar_profesion(texto):

    # 4. Verificar si el valor es nulo para evitar errores
    if pd.isna(texto):
        return texto

    # 5. Convertir el valor a texto y eliminar espacios al inicio y al final
    texto = str(texto).strip()

    # 6. Reemplazar el número "3" por la letra "e" cuando aparece entre letras
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)

    # 7. Reemplazar el símbolo "@" por la letra "a" cuando aparece entre letras
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)

    # 8. Eliminar caracteres que no sean letras o espacios
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)

    # 9. Devolver el texto limpio en minúsculas
    return texto.strip().lower()

# 10. Aplicar la función de limpieza a la columna "profesion"
df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

# 11. Diccionario con correcciones para profesiones incompletas o mal escritas
correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}

# 12. Aplicar las correcciones al DataFrame
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# 13. Calcular cuántas profesiones diferentes existen después de la limpieza
cantidad_unicas = df["profesion_limpia"].nunique()

# 14. Mostrar el resultado final
print(f"¿Cuántas profesiones únicas existen después de normalizar?:{cantidad_unicas}")