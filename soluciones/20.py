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
    fecha = re.sub(r'[ /.]', '-', fecha)  # reemplazar separadores por "-"
    fecha = re.sub(r'^(\d{2})[ -](\d{2})', r'\1\2', fecha)  # corregir formatos con espacios
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)  # buscar formato año-mes-día
    if match:
        y, m, d = match.groups()  # extraer año, mes y día
        fecha = f"{y}-{int(m):02d}-{int(d):02d}"  # asegurar formato YYYY-MM-DD
    return fecha  # devolver fecha limpia

# aplicar limpieza
df["fecha_nacimiento_limpia"] = df["fecha_nacimiento"].apply(limpiar_fecha)
# aplicar función a toda la columna

# convertir a datetime, ignorando errores
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')
# convertir a fecha válida

# filtrar fechas entre 1990 y 2000 
inicio = pd.Timestamp('1990-01-01')  # fecha inicial
fin = pd.Timestamp('2000-12-31')  # fecha final
mask = (df["fecha_nacimiento_dt"] >= inicio) & (df["fecha_nacimiento_dt"] <= fin)
# crear filtro de fechas

# contar registros
cantidad_1990_2000 = mask.sum()
# contar personas en ese rango

# resultado
print(f"Cantidad de personas nacidas entre 1990 y 2000 (inclusive): {cantidad_1990_2000}")
# mostrar resultado