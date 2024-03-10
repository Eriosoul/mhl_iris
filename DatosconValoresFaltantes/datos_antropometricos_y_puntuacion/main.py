"""
Cargar el conjunto de datos desde un archivo CSV: Utiliza pandas para cargar los datos desde el archivo CSV proporcionado.

Identificar valores faltantes: Examina el conjunto de datos para identificar qué columnas contienen valores faltantes
y cuántos hay en cada una.

Manejo de valores faltantes: Decide cómo manejar los valores faltantes. Puedes optar por eliminar las filas con valores faltantes, reemplazarlos por algún valor estadístico como la media o la mediana, o utilizar técnicas más avanzadas como la imputación.

Mostrar los datos después del manejo de valores faltantes: Muestra los datos después de haber aplicado la estrategia de manejo de valores faltantes.

Verificar si aún hay valores faltantes: Verifica si aún quedan valores faltantes en el conjunto de datos después del manejo.
"""

import pandas as pd

# Cargar el conjunto de datos desde un archivo CSV
df = 'datos_faltantes.csv'
data = pd.read_csv(df)

# Identificar valores faltantes
valores_faltantes = data.isnull().sum()
print("Valores faltantes por columna:")
print(valores_faltantes)

# Manejo de valores faltantes
# Aquí puedes decidir cómo manejar los valores faltantes, por ejemplo, eliminando las filas o imputando valores
# Por ejemplo, para eliminar las filas con valores faltantes:
data_sin_faltantes = data.dropna()

# Mostrar los datos después del manejo de valores faltantes
print("Datos después del manejo de valores faltantes:")
print(data_sin_faltantes.head())

# Verificar si aún hay valores faltantes
valores_faltantes_despues = data_sin_faltantes.isnull().sum()
print("Valores faltantes después del manejo:")
print(valores_faltantes_despues)

