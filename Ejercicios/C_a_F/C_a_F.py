# import tensorflow as tf
# import numpy as np
#
# celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
# fahrenheint = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
#
# # capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# # modelo = tf.keras.Sequential([capa])
#
# # que pasaria si añadimos mas capas
#
# oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
# oculta2 = tf.keras.layers.Dense(units=3)
# salida = tf.keras.layers.Dense(units=1)
# modelo = tf.keras.Sequential([oculta1, oculta2, salida])
#
# modelo.compile(
#     optimizer=tf.keras.optimizers.Adam(0.1),
#     loss='mean_squared_error'
# )
#
# print('Entrenamiento...')
# historial = modelo.fit(celsius, fahrenheint, epochs=10000, verbose=False)
# print('Modelo entrenado')
#
#
# import matplotlib.pyplot as plt
# plt.xlabel("# Epoca")
# plt.ylabel("Magnitud de perdida")
# plt.plot(historial.history["loss"])
#
# print("predicion")
# resultado = modelo.predict([100.0])
# print("El resultado es", str(resultado), "faherenheit!")
#
#
# print("variables inernas del modelo")
# # print(capa.get_weights())
# print(oculta1.get_weights())
# print(oculta2.get_weights())
# print(salida.get_weights())


# activacion relu
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Definir el modelo con múltiples capas
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=3, input_shape=[1], activation='relu'),  # Capa oculta con función de activación ReLU
    tf.keras.layers.Dense(units=3, activation='relu'),  # Segunda capa oculta con función de activación ReLU
    tf.keras.layers.Dense(units=1)  # Capa de salida
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Entrenamiento del modelo
print('Entrenando el modelo...')
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print('Modelo entrenado')

# Visualizar la pérdida durante el entrenamiento
plt.plot(historial.history['loss'])
plt.xlabel('Época')
plt.ylabel('Magnitud de pérdida')
plt.title('Pérdida durante el entrenamiento')
plt.show()

# Realizar una predicción con el modelo entrenado
print('Predicción:')
resultado = modelo.predict([100.0])
print('El resultado es', resultado[0][0], 'grados Fahrenheit')

# Mostrar las variables internas del modelo
print('Variables internas del modelo:')
for capa in modelo.layers:
    print(capa.get_weights())
