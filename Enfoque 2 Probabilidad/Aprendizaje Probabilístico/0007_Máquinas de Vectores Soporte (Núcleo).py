## Máquina de Vectores Soporte (modo Núcleo) con perceptrón de kernel simple para clasificación binaria.
## f(x) = sign(∑ᵢ αᵢ yᵢ K(xᵢ, x)); aquí entrenamos α con perceptrón para ilustrar el truco del kernel.

import random
import math

# RECORDATORIO: definimos un kernel RBF (gaussiano) con ancho σ
def kernel_rbf(x, y, sigma=1.0):
    # RECORDATORIO: distancia al cuadrado entre vectores
    dist2 = sum((xi - yi)**2 for xi, yi in zip(x, y))
    return math.exp(-dist2 / (2 * sigma**2))

# RECORDATORIO: datos de entrenamiento (pocos puntos 2D) con etiqueta +1 o -1
datos = [
    ([1.0, 2.0],  1),
    ([2.0, 3.0],  1),
    ([3.0, 3.0],  1),
    ([6.0, 5.0], -1),
    ([7.0, 7.0], -1),
    ([8.0, 6.0], -1),
]

# RECORDATORIO: inicializamos coeficientes α en cero
alpha = [0.0 for _ in datos]

# RECORDATORIO: etiquetas y características separadas para comodidad
X = [x for x, y in datos]
Y = [y for x, y in datos]

# RECORDATORIO: entrenamiento con perceptrón de kernel por T épocas
T = 5
for _ in range(T):
    for i, (xi, yi) in enumerate(datos):
        # RECORDATORIO: comparamos la predicción con la etiqueta
        s = 0.0
        for j in range(len(datos)):
            s += alpha[j] * Y[j] * kernel_rbf(X[j], xi)
        # RECORDATORIO: si comete error, aumentamos αᵢ
        if yi * s <= 0:
            alpha[i] += 1.0

# RECORDATORIO: función predict que usa los α aprendidos
def predict(x_new):
    s = 0.0
    for j in range(len(X)):
        s += alpha[j] * Y[j] * kernel_rbf(X[j], x_new)
    return 1 if s >= 0 else -1

nuevos = [[2.5, 2.5], [5.0, 5.0], [7.5, 5.5]]
for pt in nuevos:
    etiqueta = predict(pt)
    print(f"Punto {pt} → clase {etiqueta}")
