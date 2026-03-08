# 1. Importar librerías necesarias para el análisis de datos y uso de expresiones regulares
import pandas as pd
import re

# 2. Cargar el dataset desde el archivo CSV
df = pd.read_csv("data/personas.csv")

# 3. Función para limpiar y normalizar la columna profesión
def limpiar_profesion(texto):

    # 4. Si el valor es nulo (NaN), se devuelve sin modificar
    if pd.isna(texto):
        return texto
    
    # 5. Convertir el texto a string y eliminar espacios al inicio y al final
    texto = str(texto).strip()

    # 6. Corregir errores comunes de escritura reemplazando "3" por "e"
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)

    # 7. Corregir errores comunes reemplazando "@" por "a"
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)

    # 8. Eliminar caracteres que no sean letras o espacios
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)

    # 9. Devolver el texto limpio y en minúsculas
    return texto.strip().lower()

# 10. Aplicar la función de limpieza a la columna "profesion"
df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

# 11. Diccionario para corregir profesiones incompletas o mal escritas
correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}

# 12. Aplicar las correcciones residuales al DataFrame
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# 13. Contar cuántos registros tienen la profesión "programador"
cantidad_programadores = (df["profesion_limpia"] == "programador").sum()

# 14. Mostrar el resultado final
print(f"¿Cuántos registros tienen la profesión 'Programador' después de limpiar?: {cantidad_programadores}")