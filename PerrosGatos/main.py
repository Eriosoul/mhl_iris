import tensorflow as tf
import tensorflow_datasets as tfds

# descargar el set de datos de perros y gato
datos, metodos = tfds.load('cats_vs_dogs', as_supervised=True, with_info=True)