import pandas as pd  # importar pandas
import re  # importar expresiones regulares

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# limpiar caracteres extra y espacios
df["activo_str"] = df["activo"].astype(str).str.strip()  
# convertir a texto y eliminar espacios

df["activo_str"] = df["activo_str"].str.replace(r'[^a-zA-Z0-9áéíóúñ]', '', regex=True)  
# eliminar caracteres especiales

# normalizar a minusculas
df["activo_str"] = df["activo_str"].str.lower()  
# convertir texto a minúsculas

# mapear valores conocidos a booleano
df["activo_bool"] = df["activo_str"].map({
    "true": True,   # valores que indican activo
    "1": True,
    "si": True,
    "sí": True,
    "s": True,
    "yes": True,
    "false": False, # valores que indican inactivo
    "0": False,
    "no": False,
    "n": False
}).fillna(False)  
# valores no reconocidos se convierten en False

# contar registros con activo False
cantidad_activo_false = (~df["activo_bool"]).sum()  
# contar registros inactivos

# resultado
print(f"Cantidad de registros con activo=False: {cantidad_activo_false}")  
# mostrar resultado