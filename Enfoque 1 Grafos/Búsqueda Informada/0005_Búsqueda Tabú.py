## Búsqueda Tabú es una búsqueda informada que permite moverse a peores soluciones para escapar de óptimos locales, registrando movimientos prohibidos en una lista tabú.
## f(n) = h(n), donde h es la estimación de la distancia o costo al objetivo, pero evitando ciclos.
## Aumenta la posibilidad de encontrar mejores soluciones globales en espacios de búsqueda complejos.
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

def busqueda_tabu(grafo, heuristica, inicio, objetivo, max_iteraciones=50):
    actual = inicio
    camino = [inicio]
    lista_tabu = set()

    for _ in range(max_iteraciones):
        if actual == objetivo:
            return camino

        vecinos = [(heuristica.get(vecino, float('inf')), vecino) for vecino, _ in grafo.get(actual, []) if vecino not in lista_tabu]

        if not vecinos:
            break

        mejor_h, mejor_vecino = min(vecinos)

        lista_tabu.add(actual)
        actual = mejor_vecino
        camino.append(actual)

    if actual == objetivo:
        return camino
    else:
        return None

# Objetivo
inicio = 'Pan'
objetivo = 'PlayStation'

camino = busqueda_tabu(tienda, heuristica, inicio, objetivo)

# Resultados
print(f"\nRuta tentativa de compras desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

