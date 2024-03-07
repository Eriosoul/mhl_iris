"""
Análisis de Datos de Estudiantes

Carga de Datos: Carga un conjunto de datos de estudiantes desde un archivo CSV.
Puedes encontrar uno fácilmente en línea o utilizar un conjunto de datos de ejemplo de bibliotecas
como seaborn o scikit-learn.

Exploración de Datos: Utiliza métodos como head(), info(), describe(), y shape para comprender la estructura
y el contenido de los datos. ¿Cuántas filas y columnas tiene el conjunto de datos?
¿Qué tipo de información contiene cada columna?

Visualización de Datos: Crea visualizaciones simples para entender mejor los datos.
Por ejemplo, puedes crear histogramas para las variables numéricas, gráficos de barras para variables categóricas,
o un gráfico de dispersión para ver la relación entre dos variables.

Análisis Exploratorio de Datos: Realiza un análisis exploratorio más detallado para responder
preguntas específicas sobre los datos. Por ejemplo,
¿hay alguna correlación entre las calificaciones de matemáticas y las de ciencias?
¿Cómo se distribuyen las calificaciones en general?

Conclusiones: Extrae conclusiones y observaciones clave de tu análisis.
¿Qué tendencias o patrones has encontrado? ¿Hay alguna información interesante o inesperada en los datos?
"""

import pandas as pd

df = "estudiantes.csv"
data = pd.read_csv(df)
"""
Exploración de Datos: Utiliza métodos como head(), info(), describe(), y shape para comprender la estructura
y el contenido de los datos. ¿Cuántas filas y columnas tiene el conjunto de datos?
¿Qué tipo de información contiene cada columna?
"""
print("Head :")
print(data.head())
print("Info :")
print(data.info())
print("Describe :")
print(data.describe())

"""
Visualización de Datos: Crea visualizaciones simples para entender mejor los datos.
Por ejemplo, puedes crear histogramas para las variables numéricas, gráficos de barras para variables categóricas,
o un gráfico de dispersión para ver la relación entre dos variables.
"""
import matplotlib.pyplot as plt
import seaborn as sns
# Visualización de Datos histogramas
plt.figure(figsize=(10, 6))
plt.scatter(data['Calificacion_Matematicas'], data['Calificacion_Ciencias'], marker='o', color='r')
plt.title("Gráfico de Dispersión: Calificación de Matemáticas vs. Calificación de Ciencias")
plt.xlabel("Calificación de Matemáticas")
plt.ylabel("Calificación de Ciencias")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de dispersión con seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Calificacion_Matematicas', y='Calificacion_Ciencias', color='b')
plt.title("Gráfico de Dispersión: Calificación de Matemáticas vs. Calificación de Ciencias")
plt.xlabel("Calificación de Matemáticas")
plt.ylabel("Calificación de Ciencias")
plt.grid(True)
plt.show()

"""
Análisis Exploratorio de Datos: Realiza un análisis exploratorio más detallado para responder
preguntas específicas sobre los datos. Por ejemplo,
¿hay alguna correlación entre las calificaciones de matemáticas y las de ciencias?
¿Cómo se distribuyen las calificaciones en general?
"""
# coorelacion
correlacion = data['Calificacion_Matematicas'].corr(data['Calificacion_Ciencias'])
print("La correalacion entre matematicas y ciencias: ", correlacion)
# Distribución de las calificaciones en general
plt.figure(figsize=(10, 6))
plt.hist(data['Calificacion_Matematicas'], bins=10, alpha=0.5, label='Matemáticas')
plt.hist(data['Calificacion_Ciencias'], bins=10, alpha=0.5, label='Ciencias')
plt.title("Distribución de las Calificaciones")
plt.xlabel("Calificaciones")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.show()

# Extra

masculino = data[data['Genero'] == 'Masculino']
femenino = data[data['Genero'] == 'Femenino']

# calculo de estadisticas y depuracion de datos
masculino_mean = masculino[['Calificacion_Matematicas', 'Calificacion_Ciencias']].mean()
femenino_mean = femenino[['Calificacion_Matematicas', 'Calificacion_Ciencias']].mean()


#visualizar los datos
plt.figure(figsize=(10, 6))
masculino_mean.plot(kind='bar', color='blue', alpha=0.5, label='Masculino')
femenino_mean.plot(kind='bar', color='red', alpha=0.5, label='Femenino')
plt.title("Comparación de Calificaciones por Género")
plt.xlabel("Asignatura")
plt.ylabel("Calificación Promedio")
plt.xticks(rotation=0)
plt.legend()
plt.grid(True)
plt.show()