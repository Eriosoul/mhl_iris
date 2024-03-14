import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento
ancho = np.array([1, 4, 2, 5, 3, 6], dtype=float)
largo = np.array([2, 6, 3, 7, 4, 8], dtype=float)
area = ancho * largo  # Calcular el área correctamente

# Normalizar los datos de entrada
ancho_norm = (ancho - np.mean(ancho)) / np.std(ancho)
largo_norm = (largo - np.mean(largo)) / np.std(largo)

# Definir modelo
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[2], activation='relu')
oculta2 = tf.keras.layers.Dense(units=3, activation='relu')
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

# Compilar el modelo
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Entrenar el modelo
print("Entrenando...")
historial = modelo.fit(np.column_stack((ancho_norm, largo_norm)), area, epochs=2000, verbose=False)

# Graficar la pérdida durante el entrenamiento
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

# Predicción
nuevo_ancho_largo = np.array([[7, 3]], dtype=float)  # Crear un array bidimensional para la predicción
nuevo_ancho_largo_norm = (nuevo_ancho_largo - np.mean(ancho)) / np.std(ancho)  # Normalizar los nuevos datos
prediccion = modelo.predict(nuevo_ancho_largo_norm)
print("Predicción de área para un rectángulo con ancho=7 y largo=3:", prediccion)
