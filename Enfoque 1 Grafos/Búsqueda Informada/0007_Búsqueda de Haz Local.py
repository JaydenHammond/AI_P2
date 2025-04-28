## Búsqueda de Haz Local es una búsqueda informada que mantiene k estados simultáneamente y escoge los mejores sucesores según heurística.
## f(n) = h(n), donde h es la estimación del costo; se exploran múltiples caminos en paralelo para evitar óptimos locales.

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

def busqueda_haz_local(grafo, heuristica, inicio, objetivo, k_beams=2, max_iter=50):
    haz = [(inicio, [inicio])] * k_beams

    for _ in range(max_iter):
        for nodo, camino in haz:
            if nodo == objetivo:
                return camino

        candidatos = []
        for nodo, camino in haz:
            for vecino, coste in grafo.get(nodo, []):
                if vecino not in camino:
                    nuevos_camino = camino + [vecino]
                    candidatos.append((vecino, nuevos_camino))

        if not candidatos:
            break

        candidatos.sort(key=lambda x: heuristica.get(x[0], float('inf')))

        haz = candidatos[:k_beams]

    for nodo, camino in haz:
        if nodo == objetivo:
            return camino
    return None

# Objetivo
inicio = 'Entrada'
objetivo = 'Tesoro'


camino = busqueda_haz_local(mazmorra, heuristica, inicio, objetivo, k_beams=2)

print(f"\nRuta tentativa desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

