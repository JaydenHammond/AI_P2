## Búsqueda de Ascensión de Colinas es una búsqueda informada que elige siempre el vecino con mejor heurística, subiendo hacia el objetivo.
## f(n) = h(n), donde h es la estimación de la distancia o costo al objetivo.
## Puede atascarse en óptimos locales y no garantiza encontrar la mejor solución.
import heapq

# Productos y sus promociones de compra 1 y llévate otro
tienda = {
    'Pan': [('Huevos', 2), ('Leche', 1)],
    'Leche': [('Queso', 5), ('Pan', 1)],
    'Huevos': [('Cereal', 4)],
    'Cereal': [('Yogurt', 3)],
    'Queso': [('Yogurt', 1)],
    'Yogurt': [('PlayStation', 2)],
    'PlayStation': []
}

# Estimación del costo hasta llegar al PlayStation
heuristica = {
    'Pan': 7,
    'Leche': 6,
    'Huevos': 5,
    'Cereal': 4,
    'Queso': 5,
    'Yogurt': 2,
    'PlayStation': 0
}

def busqueda_ascension_colinas(grafo, heuristica, inicio, objetivo):
    actual = inicio
    camino = [inicio]
    visitados = set()

    while actual != objetivo:
        visitados.add(actual)
        vecinos = [(heuristica.get(vecino, float('inf')), vecino) for vecino, _ in grafo.get(actual, []) if vecino not in visitados]
        
        if not vecinos:
            break

        mejor_h, mejor_vecino = min(vecinos)

        if heuristica[actual] <= mejor_h:
            break

        actual = mejor_vecino
        camino.append(actual)

    if actual == objetivo:
        return camino
    else:
        return None

# Objetivo
inicio = 'Pan'
objetivo = 'PlayStation'

camino = busqueda_ascension_colinas(tienda, heuristica, inicio, objetivo)

print(f"\nRuta tentativa de compras desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))
