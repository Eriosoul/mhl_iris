"""
Cargar un conjunto de datos desde un archivo CSV que contenga tanto características numéricas como categóricas.
Identificar las características categóricas en el conjunto de datos.
Aplicar codificación one-hot a las características categóricas para convertirlas en variables binarias.
Normalizar las características numéricas para asegurarse de que todas estén en la misma escala.
Dividir el conjunto de datos en conjuntos de entrenamiento y prueba para poder evaluar el rendimiento del modelo.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos
df = "data_onehot.csv"
data = pd.read_csv(df)

# Identificar características categóricas
cat_features = data.select_dtypes(include=["object", "category"]).columns

# Aplicar codificación one-hot a las características categóricas
cat_data = pd.get_dummies(data[cat_features], drop_first=True, dummy_na=True)

# Eliminar características categóricas del conjunto de datos original
data.drop(cat_features, axis=1, inplace=True)

# Concatenar características codificadas con el conjunto de datos original
data = pd.concat([data, cat_data], axis=1)

# Dividir el conjunto de datos en características y etiquetas
X = data.drop('target', axis=1)   # Características
y = data['target']

# Normalizar características numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Ahora puedes usar X_train, X_test, y_train, y y_test para entrenar y evaluar tu modelo
# Inicializar el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo con el conjunto de entrenamiento
model.fit(X_train, y_train)

# Predecir las etiquetas para el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)