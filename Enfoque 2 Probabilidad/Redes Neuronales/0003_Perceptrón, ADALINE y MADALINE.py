## Estos tres modelos son redes neuronales simples para clasificación.
## El Perceptrón usa una activación escalón, ADALINE usa salida lineal con error continuo, y MADALINE es una red con varias ADALINE en paralelo.

import random  # Recordatorio: se usa para iniciar pesos aleatorios

# Función escalón: usada como activación en el Perceptrón
def escalon(x):
    return 1 if x >= 0 else 0

# Entrenamiento de un Perceptrón simple
def entrenar_perceptron(entradas, salidas, tasa=0.1, epocas=10):
    pesos = [random.uniform(-1, 1) for _ in range(len(entradas[0]))]
    sesgo = random.uniform(-1, 1)

    for _ in range(epocas):
        for i in range(len(entradas)):
            suma = sum([x * w for x, w in zip(entradas[i], pesos)]) + sesgo
            pred = escalon(suma)
            error = salidas[i] - pred
            # Recordatorio: si hay error, ajustamos pesos y sesgo
            pesos = [w + tasa * error * x for w, x in zip(pesos, entradas[i])]
            sesgo += tasa * error

    return pesos, sesgo

# Entrenamiento de una sola neurona ADALINE
def entrenar_adaline(entradas, salidas, tasa=0.1, epocas=10):
    pesos = [random.uniform(-1, 1) for _ in range(len(entradas[0]))]
    sesgo = random.uniform(-1, 1)

    for _ in range(epocas):
        for i in range(len(entradas)):
            salida = sum([x * w for x, w in zip(entradas[i], pesos)]) + sesgo
            error = salidas[i] - salida
            pesos = [w + tasa * error * x for w, x in zip(pesos, entradas[i])]
            sesgo += tasa * error

    return pesos, sesgo

# MADALINE: red de varias ADALINE que promedian sus salidas
def entrenar_madaline(entradas, salidas, tasa=0.1, epocas=10):
    # Creamos dos ADALINE en paralelo
    neuronas = [entrenar_adaline(entradas, salidas, tasa, epocas),
                entrenar_adaline(entradas, salidas, tasa, epocas)]

    return neuronas

# Datos para prueba (OR lógico)
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salidas = [0, 1, 1, 1]

# Entrenar los tres modelos
pesos_p, sesgo_p = entrenar_perceptron(entradas, salidas)
pesos_a, sesgo_a = entrenar_adaline(entradas, salidas)
madaline = entrenar_madaline(entradas, salidas)

# Resultados Perceptrón
print("\nPredicciones del Perceptrón:")
for e in entradas:
    salida = escalon(sum([x * w for x, w in zip(e, pesos_p)]) + sesgo_p)
    print(f"{e} -> {salida}")

# Resultados ADALINE
print("\nPredicciones de ADALINE:")
for e in entradas:
    salida = sum([x * w for x, w in zip(e, pesos_a)]) + sesgo_a
    print(f"{e} -> {round(salida, 2)}")  # Recordatorio: la salida es continua

# Resultados MADALINE (promedio de las salidas de dos ADALINE)
print("\nPredicciones de MADALINE (promedio de 2 ADALINE):")
for e in entradas:
    salidas_individuales = []
    for pesos, sesgo in madaline:
        salida = sum([x * w for x, w in zip(e, pesos)]) + sesgo
        salidas_individuales.append(salida)
    promedio = sum(salidas_individuales) / len(salidas_individuales)
    print(f"{e} -> {round(promedio, 2)}")
