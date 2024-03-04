import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# cargar el conjunto de datos de iris
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# convertir el target en tipo categórico
data['target'] = data['target'].map({0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})

# gráfico de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='sepal length (cm)', y='sepal width (cm)', hue='target', style='target')
plt.title("Gráfico de Dispersión de Iris")
plt.show()

# historgrama
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='petal length (cm)', kde=True)
plt.title("Histograma de la longitud del petalo")
plt.show()

# Grafico de barras
plt.figure(figsize=(10, 6))
data['target'].value_counts().plot(kind='bar')
plt.title("Distribución de las clases de iris")
plt.xlabel("Clases")
plt.ylabel("Cantidad")
plt.show()

# Mapa de calor
plt.figure(figsize=(10, 8))
correlation_matrix = data.drop('target', axis=1).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Mapa de calor")
plt.show()

