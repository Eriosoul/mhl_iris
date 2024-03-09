"""
Cargar un conjunto de datos desde un archivo CSV.
Realizar una exploración inicial de los datos para comprender su estructura y contenido.
Realizar una limpieza de datos si es necesario
(manejo de valores faltantes, eliminación de columnas innecesarias, etc.).
Calcular estadísticas descriptivas sobre las variables numéricas del conjunto de datos.
Visualizar la distribución de las variables numéricas utilizando histogramas.
Realizar un análisis exploratorio de los datos para identificar posibles patrones o relaciones entre las variables.
Plantear preguntas y buscar respuestas a través del análisis de los datos.
¿Te parece bien? Si estás listo,
¿quieres que te proporcione un conjunto de datos para trabajar o prefieres usar uno específico que tengas en mente?

"""

import pandas as pd
import matplotlib.pyplot as plt
# Cargar un conjunto de datos desde un archivo CSV. 
df = 'datos.csv'

data = pd.read_csv(df)
print(data.head())
print(len(data))
print(data.describe())

# Visualizar la distribución de las variables numéricas utilizando histogramas.
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(data['Edad'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribución de la Edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 2)
plt.hist(data['Altura(cm)'], bins=10, color='salmon', edgecolor='black')
plt.title('Distribución de la Altura')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 3)
plt.hist(data['Peso(kg)'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribución del Peso')
plt.xlabel('Peso (kg)')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 4)
plt.hist(data['Puntuacion'], bins=10, color='orange', edgecolor='black')
plt.title('Distribución de la Puntuación')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()


"""
suploat: para saber loque hace
El método subplot() en Matplotlib se utiliza para crear una disposición de subtramas dentro de una figura principal.
 Esto es útil cuando se desea mostrar múltiples gráficos en una sola figura. La disposición de las subtramas se 
 especifica mediante el número de filas y columnas, así como el índice de la subtrama actual.

Aquí está cómo funciona:

El método subplot() toma tres argumentos: el número de filas, el número de columnas y el índice de la subtrama actual.
El índice de la subtrama comienza desde 1 en la esquina superior izquierda y aumenta hacia la derecha y hacia abajo.
Se pueden especificar múltiples subtramas en una sola llamada a subplot() utilizando 
la convención de indexación de fila por fila.
Por ejemplo, subplot(2, 2, 1) especifica una disposición de subtramas de 2 filas y 2 columnas, y selecciona 
la primera subtrama como la subtrama actual. Luego, subplot(2, 2, 2) selecciona la segunda subtrama en la primera fila, 
y así sucesivamente.

En el código proporcionado anteriormente, se están creando 4 subtramas para mostrar histogramas de 4 variables 
diferentes (Edad, Altura(cm), Peso(kg) y Puntuacion). Cada subtrama se configura usando subplot(), y luego se crea un 
histograma en cada subtrama usando plt.hist(). Esto resulta en una sola figura con múltiples histogramas distribuidos 
en una cuadrícula
"""