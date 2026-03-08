import pandas as pd  # importar pandas

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# convertir a string
df["salario_str"] = df["salario"].astype(str)  # convertir salarios a texto

# reemplazos de letras y eliminación de "aprox."
reemplazos = {
    "l": "1",      # corregir l por 1
    "O": "0",      # corregir O por 0
    "e": "3",      # corregir e por 3
    "aprox.": ""   # eliminar "aprox."
}

for old, new in reemplazos.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)
    # aplicar cada reemplazo

# reemplazar comas por puntos
df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)
# usar punto como separador decimal

# eliminar cualquier caracter que no sea digito o punto
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)
# dejar solo números y punto

# convertir a float
df["salario_limpio"] = df["salario_limpio"].astype(float)
# convertir a número decimal

# calcular salario maximo
salario_maximo = df["salario_limpio"].max()
# obtener el salario más alto

# resultado
print(round(salario_maximo, 0))
# mostrar resultado redondeado