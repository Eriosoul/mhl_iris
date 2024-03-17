import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1)

# Definir el modelo de regresión lineal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])  # Capa densa lineal
])

# Compilar el modelo
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Entrenar el modelo
historial = modelo.fit(X, y, epochs=100, verbose=0)

# Obtener los pesos del modelo entrenado
pesos = modelo.layers[0].get_weights()
pendiente = pesos[0][0][0]
intercepto = pesos[1][0]

# Visualizar el modelo y los datos
plt.scatter(X, y, label='Datos de entrenamiento')
plt.plot(X, pendiente * X + intercepto, color='red', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Regresión lineal con TensorFlow')
plt.show()