# Redes Neuronales Convolucionales

# Primer ejemplo : entrenamiento de numeros
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

# Recolectando los datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Construcción del modelo
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2))) # reduce las dimensiones a 2 * 2 = 4 pero los reducimos a 1
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2))) # volvemos a reducir la imagen dividiendo entre 2 para sintetizar 4 pixeles entre 2
model.add(Flatten())
model.add(Dense(128, activation='relu'))  # Modifiqué el número de neuronas
model.add(Dense(10, activation='softmax'))# softmax para clasificacion categorica

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# entrenamos el modelo con los datos del entrenamiento
model.fit(x_train, y_train, epochs=10)

score = model.evaluate(x_test, y_test, verbose=0)
print("Test accuracy:", score[1])


import numpy as np

# ejemplo de imagen
img = np.expand_dims(x_test[0], axis=0)

# prediccion
prediction = model.predict(img)

# etiqueta de la prediccion
label = np.argmax(prediction)
print('Preddiction: ', label)
