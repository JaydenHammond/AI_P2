## Búsqueda Voraz Primero el Mejor es una búsqueda informada que usa solo la heurística para guiarse hacia el objetivo.
## f(n) = h(n), donde h es la estimación de la distancia o costo al objetivo.
## No garantiza el camino más barato, pero puede encontrar rutas rápidas si la heurística es adecuada.
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

def busqueda_voraz_primero_mejor(grafo, heuristica, inicio, objetivo):
    cola = [(heuristica[inicio], [inicio])]
    visitados = set()

    while cola:
        h, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo in visitados:
            continue
        visitados.add(nodo)

        for vecino, _ in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola, (heuristica.get(vecino, float('inf')), camino + [vecino]))

    return None

# Objetivo
inicio = 'Pan'
objetivo = 'PlayStation'

camino = busqueda_voraz_primero_mejor(tienda, heuristica, inicio, objetivo)

# Resultados
print(f"\nRuta de compras tentativa desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

