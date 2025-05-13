## Funciones de Activación determinan cómo responde una neurona artificial a la entrada. Se usan para introducir no linealidad al modelo y permitir aprender patrones complejos.
## f(x) puede ser lineal, sigmoide, ReLU o tanh, y cada una tiene sus propias características útiles según el problema.

import math  #RECORDATORIO: math es útil para funciones como exp y tanh

#RECORDATORIO: función lineal - salida igual a la entrada (sin transformación)
def lineal(x):
    return x

#RECORDATORIO: función sigmoide - comprime la salida entre 0 y 1
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

#RECORDATORIO: función tangente hiperbólica - salida entre -1 y 1
def tanh(x):
    return math.tanh(x)

#RECORDATORIO: ReLU - salida 0 si es negativa, x si es positiva
def relu(x):
    return max(0, x)

#RECORDATORIO: ejemplo para comparar salidas de funciones de activación
valores = [-2, -1, 0, 1, 2]

print("Comparación de funciones de activación:")
for x in valores:
    print(f"\nEntrada: {x}")
    print(f"Lineal: {lineal(x)}")
    print(f"Sigmoide: {round(sigmoide(x), 3)}")
    print(f"Tanh: {round(tanh(x), 3)}")
    print(f"ReLU: {relu(x)}")
