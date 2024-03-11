"""
Cargar un conjunto de datos desde un archivo CSV que contenga tanto características numéricas como categóricas.
Identificar las características categóricas en el conjunto de datos.
Aplicar codificación one-hot a las características categóricas para convertirlas en variables binarias.
Normalizar las características numéricas para asegurarse de que todas estén en la misma escala.
Dividir el conjunto de datos en conjuntos de entrenamiento y prueba para poder evaluar el rendimiento del modelo.
"""

import pandas as pd
