## Búsqueda Online es una búsqueda informada que explora el espacio de soluciones sin conocimiento completo del mismo.
## f(n) = h(n), donde h es la estimación del costo; se busca solución conforme se explora el grafo sin tener todo el mapa desde el inicio.

import random

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

def busqueda_online(grafo, heuristica, inicio, objetivo):
    """
    graf o: dict de adyacencia con costes
    heuristica: dict con estimación h(n)
    inicio: nodo inicial
    objetivo: nodo meta
    """
    actual = inicio
    camino = [inicio]
    explorado = set()

    while actual != objetivo:
        explorado.add(actual)
        vecinos = grafo.get(actual, [])
        if not vecinos:
            break
        
        vecinos_no_explorados = [(v, c) for v, c in vecinos if v not in explorado]

        if not vecinos_no_explorados:
            break

        # Elegir el vecino con mejor heurística
        vecino = min(vecinos_no_explorados, key=lambda x: heuristica.get(x[0], float('inf')))[0]

        actual = vecino
        camino.append(actual)

    if actual == objetivo:
        return camino
    else:
        return None

# Objetivo
inicio = 'Entrada'
objetivo = 'Tesoro'

camino = busqueda_online(mazmorra, heuristica, inicio, objetivo)

print(f"\nRuta tentativa desde '{inicio}' hasta '{objetivo}' usando Búsqueda Online:")
print(" -> ".join(camino))

