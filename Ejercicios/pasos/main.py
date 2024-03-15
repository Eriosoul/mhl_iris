import tensorflow as tf

entrada = tf.constant([[0.3, 0.2, 0.1]], dtype=tf.float32)
pasos = tf.Variable(tf.random.normal(shape=(3, 1)), datype=tf.float32)

def suming(x):
    return 1 / (1 + tf.exp(-x))

suma_progresada = tf.matmul(entrada, pasos)

salida = suming(suma_progresada)
print("La informacion da: ", salida)