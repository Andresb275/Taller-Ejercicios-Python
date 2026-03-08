import pandas as pd  # importar pandas

# cargar dataset
df = pd.read_csv("data/personas.csv")  # leer archivo CSV

# detectar salarios con caracteres no numéricos
salarios_no_numericos = ~df["salario"].astype(str).str.match(r'^\d+$')
# verificar si salario contiene algo diferente a números

# contar registros
cantidad_salarios_no_numericos = salarios_no_numericos.sum()
# contar cuántos salarios no son numéricos

print("Registros con salario que contiene caracteres no numéricos:", cantidad_salarios_no_numericos)
# mostrar resultado