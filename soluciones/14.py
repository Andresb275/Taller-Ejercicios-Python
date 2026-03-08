import pandas as pd  # importar pandas

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# convertir a string
df["salario_str"] = df["salario"].astype(str)  # convertir salarios a texto

# reemplazos de letras y eliminacion de "aprox."
reemplazos = {
    "l": "1",      # corregir l por 1
    "O": "0",      # corregir O por 0
    "e": "3",      # corregir e por 3
    "aprox.": ""   # eliminar la palabra aprox.
}

for old, new in reemplazos.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)
    # aplicar reemplazos definidos

# reemplazar comas por puntos
df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)
# cambiar coma decimal por punto

# eliminar cualquier caracter que no sea digito o punto
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)
# dejar solo números y punto decimal

# convertir a float
df["salario_limpio"] = df["salario_limpio"].astype(float)
# convertir a número decimal

# calcular salario promedio
salario_promedio = df["salario_limpio"].mean()
# calcular promedio de salarios

# resultado
print(round(salario_promedio, 3))
# mostrar promedio redondeado a 3 decimales