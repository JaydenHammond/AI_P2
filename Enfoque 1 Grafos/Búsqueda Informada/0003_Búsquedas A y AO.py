## A* es una búsqueda informada que usa una heurística para guiarse hacia el objetivo.
## f(n) = g(n) + h(n), donde g es el costo real y h es la estimación al objetivo.
## Encuentra el camino más barato si la heurística es razonable.
import heapq

# Productos y sus promociones de compra 1 y llevate otro
tienda = {
    'Pan': [('Leche', 1), ('Cereal', 4)],
    'Leche': [('Pan', 1), ('Huevos', 2), ('Queso', 5)],
    'Cereal': [('Pan', 4), ('Yogurt', 3)],
    'Huevos': [('Leche', 2)],
    'Queso': [('Leche', 5), ('Yogurt', 1)],
    'Yogurt': [('Cereal', 3), ('Queso', 1), ('PlayStation', 2)],
    'PlayStation': [('Yogurt', 2)]
}

# Estimación del costo hasta llegar al PlayStation
heuristica = {
    'Pan': 7,
    'Leche': 6,
    'Cereal': 5,
    'Huevos': 6,
    'Queso': 4,
    'Yogurt': 2,
    'PlayStation': 0
}

def busqueda_a_estrella(grafo, heuristica, inicio, objetivo):
    cola = [(heuristica[inicio], 0, [inicio])]
    visitados = set()

    while cola:
        f, costo_actual, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino, costo_actual

        if nodo in visitados:
            continue
        visitados.add(nodo)

        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                g = costo_actual + costo
                h = heuristica.get(vecino, float('inf'))
                f = g + h
                heapq.heappush(cola, (f, g, camino + [vecino]))

    return None, float('inf')

# Objetivo
inicio = 'Pan'
objetivo = 'PlayStation'

camino, costo_total = busqueda_a_estrella(tienda, heuristica, inicio, objetivo)

# Resultados
print(f"\nRuta de compras óptima desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

