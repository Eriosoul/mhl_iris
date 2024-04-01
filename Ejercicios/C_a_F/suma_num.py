import numpy as np

# Generamos los datos sinteticos
num_sample = 1000
x = np.random.uniform(low=0, high=1000, size=(num_sample, 2))
y = np.sum(x, axis=1) # la suma de los numeros

for i in range(5):
    print("Ejemplo", i+1, "- Entrada:", x[i], "- Suma:", y[i])


import tensorflow as tf

modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(2,), activation='relu'),
    tf.keras.layers.Dense(1)
])

modelo.compile(optimizer='adam', loss='mse')

#entrenar el modelo

historial = modelo.fit(x, y, epochs=50, validation_split=0.2)

loss= modelo.evaluate(x, y)
print("Pérdida final en el conjunto de entrenamiento:", loss)