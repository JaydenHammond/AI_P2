## La Búsqueda en Grafos es similar a la búsqueda en anchura, pero evita visitar nodos repetidos.
## Ideal para grafos con ciclos o rutas que se cruzan.
## Explora nivel por nivel hasta encontrar el objetivo, sin caer en bucles infinitos.

# Facebook Friends
red_social = {
    'Jose': ['Neri', 'Alejandro', 'Julio'],
    'Neri': ['Jose', 'Alejandro'],
    'Alejandro': ['Jose', 'Neri', 'Omar'],
    'Julio': ['Jose', 'Omar'],
    'Omar': ['Alejandro', 'Julio', 'Jayden'],
    'Jayden': []
}

from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

# Buscador (poner nombres)
inicio = 'Jose'
objetivo = 'Jayden'

camino = busqueda_en_grafos(red_social, inicio, objetivo)

#Resultado
print(f"\nRuta desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

