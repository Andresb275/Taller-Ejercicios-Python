import pandas as pd
import codecs
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Diccionario para corregir ciudades alteradas
correcciones_ciudades = {
    "S@nt@ M@rt@": "Santa Marta", "V@ll3dup@r": "Valledupar",
    "M@niz@l3s": "Manizales", "Sinc3l3jo": "Sincelejo",
    "Buc@r@m@ng@": "Bucaramanga", "Tunj@": "Tunja",
    "Ib@gu3": "Ibague", "C@rt@g3n@": "Cartagena",
    "Arm3ni@": "Armenia", "M3d3llin": "Medellin",
    "Cucut@": "Cucuta", "C@li": "Cali",
    "P3r3ir@": "Pereira", "Mont3ri@": "Monteria",
    "Bogot@": "Bogota", "Vill@vic3ncio": "Villavicencio",
    "N3iv@": "Neiva", "Pop@y@n": "Popayan",
    "B@rr@nquill@": "Barranquilla", "P@sto": "Pasto"
}

# Limpiar espacios en ciudades
df["ciudad"] = df["ciudad"].str.strip()

# Corregir ciudades usando el diccionario
df["ciudad"] = df["ciudad"].replace(correcciones_ciudades)

# Eliminar caracteres especiales
df["ciudad"] = df["ciudad"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)

# Formatear ciudades (capitalizar)
df["ciudad"] = df["ciudad"].str.strip().str.title()

# Convertir columna activo a texto
df["activo_str"] = df["activo"].astype(str).str.strip()

# Eliminar caracteres no válidos
df["activo_str"] = df["activo_str"].str.replace(r'[^a-zA-Z0-9áéíóúñ]', '', regex=True)

# Convertir a minúsculas
df["activo_str"] = df["activo_str"].str.lower()

# Convertir valores a booleanos
df["activo_bool"] = df["activo_str"].map({
    "true": True,  "1": True,  "si": True,
    "sí": True,    "s": True,  "yes": True,
    "false": False, "0": False, "no": False, "n": False
}).fillna(False)

# Función para limpiar fechas
def limpiar_fecha(fecha):

    # Verificar valores nulos
    if pd.isna(fecha):
        return None

    # Convertir a texto y limpiar espacios
    fecha = str(fecha).strip()

    # Eliminar caracteres no válidos
    fecha = re.sub(r'[^0-9\-/. ]', '', fecha)

    # Unificar separadores de fecha
    fecha = re.sub(r'[ /.]', '-', fecha)

    # Corregir formatos con espacios
    fecha = re.sub(r'^(\d{2})[ -](\d{2})', r'\1\2', fecha)

    # Detectar formato año-mes-día
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)

    if match:
        y, m, d = match.groups()

        # Formatear fecha correctamente
        fecha = f"{y}-{int(m):02d}-{int(d):02d}"

    return fecha

# Limpiar fechas de nacimiento
df["fecha_nacimiento_limpia"] = df["fecha_nacimiento"].apply(limpiar_fecha)

# Convertir a tipo datetime
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')

# Definir fecha límite
limite = pd.Timestamp('1980-12-31')

# Filtrar Barranquilla, activos y nacidos después de 1980
resultado = df[
    (df["ciudad"] == "Barranquilla") &
    (df["activo_bool"] == True) &
    (df["fecha_nacimiento_dt"] > limite)
]

# Mostrar cantidad de registros
print(f"¿Cuántos registros tienen ciudad 'Barranquilla', activos y nacidos después de 1980?:{len(resultado)}")