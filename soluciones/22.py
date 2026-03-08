import pandas as pd  # importar pandas
from datetime import datetime  # importar manejo de fechas
import re  # importar expresiones regulares

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# función limpieza para fechas
def limpiar_fecha(fecha):
    if pd.isna(fecha):
        return None  # devolver None si está vacío
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

# fecha actual
fecha_actual = pd.Timestamp('2026-02-26')
# definir fecha actual para cálculo

# calcular edad
df["edad"] = (fecha_actual - df["fecha_nacimiento_dt"]).dt.days // 365
# calcular edad aproximada en años

# contar personas con mas de 50 años
cantidad_mas_50 = (df["edad"] > 50).sum()
# contar personas mayores de 50

# resultado
print(f"Cantidad de personas con más de 50 años: {cantidad_mas_50}")
# mostrar resultado