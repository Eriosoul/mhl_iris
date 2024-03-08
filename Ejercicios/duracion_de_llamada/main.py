"""
Cargar el conjunto de datos desde un archivo CSV.
Realizar una exploración inicial de los datos para entender su estructura y contenido.
Calcular estadísticas descriptivas sobre la duración de las llamadas, como la duración promedio,
la duración máxima y mínima, etc.
Crear un histograma para visualizar la distribución de la duración de las llamadas
y entender cómo se distribuyen en diferentes rangos.
Realizar un análisis exploratorio de los datos para responder preguntas como
¿cuántos usuarios hay en total?
¿cuál es la duración promedio de las llamadas?
¿hay alguna tendencia o patrón en la duración de las llamadas?
"""

import pandas as pd
import matplotlib.pyplot as plt

# paso 1
# Realizar una exploración inicial de los datos para entender su estructura y contenido.
data_frame = 'duracion.csv'

data = pd.read_csv(data_frame)
print(data.head())
print(len(data))
print(data.describe())

# paso 2
# Calcular estadísticas descriptivas sobre la duración de las llamadas, como la duración promedio,
# CODIGO ANTIGUO
# data_item = []
# promedio_data = data['Duracion']
# for item in promedio_data:
#     data_item.append(item)
#
# print(f"Los datos del array: {data_item}")
# cantidad_datos = len(data_item)
# crar_suma = sum(data_item)
# print(f"La cantidad de datos es de: {cantidad_datos}, la suma esta preparada: {crar_suma}")
# promedio = crar_suma / cantidad_datos
# print(f"La duración de las llamadas, como la duración promedio de: {promedio}")
# la duración máxima y mínima, etc.
# CODIGO MEJORADO
promedio = data['Duracion'].mean()
max_duration = data['Duracion'].max()
min_duration = data['Duracion'].min()
usuarios = len(data['Usuario'])
print(f"La cantidad de datos es de: {max_duration}, la suma esta preparada: {min_duration}")
print(f"La duracion de las llamadas, como la duracion promedio de: {promedio}")
print(f'Hay un toal de usuarios de: {usuarios}')

plt.figure(figsize=(10, 6))
plt.hist(data['Duracion'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribucion de la duracion de las llamada')
plt.ylabel('Duracion (en segundos)')
plt.xlabel('Frecuencia')
plt.grid(True)
plt.show()

# Grafico lineal
plt.figure(figsize=(10, 6))
plt.plot(data['Usuario'], data['Duracion'], marker='o', linestyle='-', color='r')
plt.xlabel('Usuarios')
plt.ylabel('Duracion (llamadas en segundos)')
plt.grid(True)
plt.show()
