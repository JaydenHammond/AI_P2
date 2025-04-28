## Búsqueda de Temple Simulado es una búsqueda informada que acepta movimientos peores con una cierta probabilidad decreciente para escapar de óptimos locales.
## f(n) = h(n), donde h es la estimación del costo, pero se permite la exploración con "temperatura".
## Es útil para encontrar soluciones cercanas al óptimo en espacios de búsqueda complejos.
import random
import math

# Grafo DND
mazmorra = {
    'Entrada': [('Sala1', 3), ('Sala2', 5)],
    'Sala1': [('Tesoro', 7)],
    'Sala2': [('Sala3', 2)],
    'Sala3': [('Tesoro', 4)],
    'Tesoro': []
}

# Heurística: distancia estimada al Tesoro
heuristica = {
    'Entrada': 10,
    'Sala1': 7,
    'Sala2': 6,
    'Sala3': 3,
    'Tesoro': 0
}

def busqueda_temple_simulado(grafo, heuristica, inicio, objetivo, temperatura_inicial=1000, tasa_enfriamiento=0.95, temperatura_minima=0.1):
    actual = inicio
    camino = [inicio]
    temperatura = temperatura_inicial

    while temperatura > temperatura_minima:
        if actual == objetivo:
            return camino

        vecinos = grafo.get(actual, [])
        if not vecinos:
            break

        vecino = random.choice(vecinos)[0]

        delta = heuristica.get(vecino, float('inf')) - heuristica.get(actual, float('inf'))

        if delta < 0 or math.exp(-delta / temperatura) > random.random():
            actual = vecino
            camino.append(actual)

        temperatura *= tasa_enfriamiento

    if actual == objetivo:
        return camino
    else:
        return None

# Objetivo
inicio = 'Entrada'
objetivo = 'Tesoro'

camino = busqueda_temple_simulado(mazmorra, heuristica, inicio, objetivo)

print(f"\nRuta tentativa desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

