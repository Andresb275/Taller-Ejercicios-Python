import pandas as pd  # importar pandas
import re  # importar expresiones regulares

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# funcion limpieza
def limpiar_fecha(fecha):
    if pd.isna(fecha):
        return None  # devolver None si la fecha está vacía
    fecha = str(fecha).strip()  # convertir a texto y quitar espacios
    fecha = re.sub(r'[^0-9\-/. ]', '', fecha)  # eliminar caracteres no válidos
    fecha = re.sub(r'[ /.]', '-', fecha)  # unificar separadores con "-"
    fecha = re.sub(r'^(\d{2})[ -](\d{2})', r'\1\2', fecha)  # corregir formatos con espacio
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)  # buscar formato año-mes-día
    if match:
        y, m, d = match.groups()  # extraer año, mes y día
        fecha = f"{y}-{int(m):02d}-{int(d):02d}"  # asegurar formato YYYY-MM-DD
    return fecha  # devolver fecha limpia

# aplicar limpieza
df["fecha_nacimiento_limpia"] = df["fecha_nacimiento"].apply(limpiar_fecha)
# limpiar todas las fechas

# convertir a datetime
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')
# convertir a tipo fecha

# filtrar fechas antes de 1960-01-01
limite = pd.Timestamp('1960-01-01')  # definir fecha límite
mask = df["fecha_nacimiento_dt"] < limite  # seleccionar fechas anteriores

# contar registros
cantidad_antes_1960 = mask.sum()
# contar personas nacidas antes de 1960

# resultado
print(f"Cantidad de personas nacidas antes de 1960: {cantidad_antes_1960}")
# mostrar resultado