import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheint = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# creamos la capa
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss="mean_squared_error"
)


print("Entrenando modelo")
historial = modelo.fit(fahrenheint, celsius, epochs=1000, verbose=False)
print("Moldelo entrenado")


import matplotlib.pyplot as plt
plt.xlabel('# Epoca')
plt.ylabel('Magnitud de perdida')
plt.plot(historial.history["loss"])


print("predicion")
resultado = modelo.predict([59.0])
print(f"El resultado es {str(resultado)} a celsius")
