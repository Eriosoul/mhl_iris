"""
paso 1: Carga de datos: Utiliza una biblioteca como pandas para cargar los datos de precios de acciones desde un archivo CSV o una fuente en línea.

Exploración de datos: Echa un vistazo a los datos para comprender su estructura y contenido.
¿Cuántos días de datos tienes? ¿Cuál es el rango de precios de cierre? ¿Hay alguna relación aparente entre el precio de cierre y el volumen de negociación?

Gráfico de línea: Crea un gráfico de línea que muestre la tendencia de los precios de cierre a lo largo del tiempo. El eje x debe representar las fechas y el eje y debe representar los precios de cierre.

Gráfico de dispersión: Crea un gráfico de dispersión que muestre la relación entre el precio de cierre y el volumen de negociación. Cada punto en el gráfico representará un día de negociación, con el precio de cierre en el eje x y el volumen en el eje y.

Personalización: Experimenta con diferentes opciones de personalización, como colores, estilos de línea, etiquetas de ejes, títulos, leyendas, etc., para hacer tus visualizaciones más claras y atractivas.
"""

import pandas as pd
# paso 1
df = "precios.csv"
data = pd.read_csv(df)

print(data.head())
print(len(data))
print(data['Precio de Cierre'].describe())

import matplotlib.pyplot as plt
import seaborn as sns
"""
Gráfico de línea: Crea un gráfico de línea que muestre la tendencia de los precios de cierre a lo largo del tiempo. 
El eje x debe representar las fechas y el eje y debe representar los precios de cierre.
"""
data = pd.read_csv(df)
# Convertir la columna 'Fecha' a formato datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])

# Gráfico de línea
plt.figure(figsize=(10, 6))
plt.plot(data['Fecha'], data['Precio de Cierre'], marker='o', linestyle='-', color='b')
plt.title("Tendencia de Precios de Cierre")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre")
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mayor legibilidad
plt.grid(True)
plt.show()
"""
Gráfico de dispersión: Crea un gráfico de dispersión que muestre la relación entre el 
precio de cierre y el volumen de negociación. Cada punto en el gráfico representará un día de negociación, 
con el precio de cierre en el eje x y el volumen en el eje y.
"""
# grafico de dimension
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Precio de Cierre', y='Volumen', color='b')
plt.title("Grafico dinamico")
plt.xlabel('Precio de Cierre')
plt.ylabel('Volumen')
plt.grid(True)
plt.show()