import numpy as np

# Generamos los datos sinteticos
num_sample = 1000
x = np.random.uniform(low=0, high=1000, size=(num_sample, 2))
y = np.sum(x, axis=1) # la suma de los numeros

for i in range(5):
    print("Ejemplo", i+1, "- Entrada:", x[i], "- Suma:", y[i])