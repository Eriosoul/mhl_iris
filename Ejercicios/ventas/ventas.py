"""
Carga de datos: Utiliza una biblioteca como pandas para cargar los datos de ventas mensuales desde un archivo CSV
o crea un DataFrame de ejemplo con datos ficticios.

Exploración de datos: Echa un vistazo a los datos para comprender su estructura y contenido.
¿Cuántos meses de datos tienes? ¿Cuál es el rango de valores de ventas?
¿Hay algún mes con ventas excepcionalmente altas o bajas?

Gráfico de línea: Crea un gráfico de línea que muestre la tendencia de las ventas a lo largo del año.
El eje x debe representar los meses y el eje y debe representar las ventas. Esto te dará una idea visual de cómo
las ventas fluctúan a lo largo del tiempo.

Gráfico de barras: Crea un gráfico de barras que muestre las ventas de cada mes por separado.
Cada barra en el gráfico representará las ventas de un mes en particular. Esto te ayudará a comparar las ventas
entre diferentes meses de manera más clara.

Histograma: Crea un histograma para visualizar la distribución de las ventas. Esto te mostrará con qué frecuencia ocurren diferentes rangos de ventas y si hay algún patrón o sesgo en los datos.

Personalización: Experimenta con diferentes opciones de personalización, como colores, etiquetas de ejes, títulos, leyendas, etc., para hacer tus visualizaciones más claras y atractivas.

Recursos:

Conjunto de datos de ventas mensuales (real o ficticio).
Bibliotecas de Python como pandas, matplotlib y seaborn para cargar datos y crear visualizaciones.
"""

# Carga de datos: Utiliza una biblioteca como pandas para cargar los datos de ventas mensuales desde un archivo CSV
# o crea un DataFrame de ejemplo con datos ficticios.
import pandas as pd

data = "ventas.csv"
df = pd.read_csv(data)
# Estructura y contenido de los datos: Utiliza df.head() para mostrar las primeras filas del
# DataFrame y observar cómo están estructurados los datos y qué tipo de información contienen.
print("Estructura y contenido de los datos: Utiliza df.head()")
print(df.head())
# Número de meses de datos: Utiliza len(df) para contar el número total de filas en el DataFrame,
# lo que te dará la cantidad de meses de datos que tienes.
print("Número de meses de datos: Utiliza len(df)")
print(len(df))
#Rango de valores de ventas: Utiliza df['Ventas'].describe()
# para obtener estadísticas descriptivas sobre la columna de ventas, incluido el rango de valores.
print("Rango de valores de ventas: Utiliza df['Ventas'].describe()")
print(df['Ventas'].describe())



import matplotlib.pyplot as plt
import seaborn as sns
"""
Gráfico de línea: Crea un gráfico de línea que muestre la tendencia de las ventas a lo largo del año.
El eje x debe representar los meses y el eje y debe representar las ventas. Esto te dará una idea visual de cómo
las ventas fluctúan a lo largo del tiempo.
"""
# Gráfico de línea
plt.figure(figsize=(10, 6))
plt.plot(df['Mes'], df['Ventas'], marker='o', linestyle='-', color='r')
plt.title("Tendencia de Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mayor legibilidad
plt.grid(True)
plt.show()
"""
Histograma: Crea un histograma para visualizar la distribución de las ventas. 
Esto te mostrará con qué frecuencia ocurren diferentes rangos de ventas y si hay algún patrón o sesgo en los datos.
"""

plt.figure(figsize=(10, 6))
sns.histplot(df['Ventas'], color='b', bins=10)
plt.title("Histograma ventas")
plt.xlabel("Ventas")
plt.ylabel("Franquicia")
plt.grid(True)
plt.show()