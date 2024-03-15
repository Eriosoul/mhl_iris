import tensorflow as tf
import numpy as np


# Precios originales y precios finales
precios_originales = np.array([4.99, 6.99, 20.59, 39.99, 66.10], dtype=float)
precios_finales = np.array([4.3413, 6.0813, 17.9133,34.7913, 57.507], dtype=float)

# Calcular el porcentaje de descuento
porcentajes_descuento = (precios_originales - precios_finales) / precios_originales


capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss="mean_squared_error"
)

print("Entrenando modelo")
historial = modelo.fit(precios_originales, porcentajes_descuento, epochs=1500, verbose=False)
print("Modelo entrenado :D")


import matplotlib.pyplot as plt
plt.xlabel('# Epoca')
plt.ylabel('Magnitud de perdida')
plt.plot(historial.history["loss"])
plt.title('Pérdida durante el entrenamiento')
plt.show()

# Realizar predicciones
precio_original_prediccion = np.array([6759.99])
descuento_prediccion = modelo.predict(precio_original_prediccion)
print(f"El modelo ha aprendido que el descuento aproximado para un precio original de {precio_original_prediccion[0]} € es de {descuento_prediccion[0][0] * 100:.2f}%")

# Calcular el precio final usando el descuento aprendido
precio_final_prediccion = precio_original_prediccion * (1 - descuento_prediccion)
print(f"Por lo tanto, el precio final sería aproximadamente: {precio_final_prediccion[0][0]} €")


print('Variables internas del modelo:')
for capa in modelo.layers:
    print(capa.get_weights())

