#La Búsqueda en Anchura (BFS) es un algoritmo que explora un grafo
#(o mapa) nivel por nivel, es decir, primero visita todos los vecinos más
#cercanos al punto de inicio antes de ir más lejos.

from collections import deque

#ciudades de Estados Unidos
mapa = {
    'New York': ['Philadelphia', 'Boston'],
    'Philadelphia': ['New York', 'Washington D.C.'],
    'Boston': ['New York', 'Chicago'],
    'Washington D.C.': ['Philadelphia', 'Atlanta'],
    'Chicago': ['Boston', 'Denver'],
    'Atlanta': ['Washington D.C.', 'Miami'],
    'Miami': ['Atlanta'],
    'Denver': ['Chicago', 'Los Angeles'],
    'Los Angeles': ['Denver', 'San Francisco'],
    'San Francisco': ['Los Angeles']
}

def buscar_camino_mas_corto(mapa, inicio, objetivo):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        ciudad = camino[-1]

        if ciudad not in visitados:
            visitados.add(ciudad)

            if ciudad == objetivo:
                return camino

            for vecino in mapa.get(ciudad, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

inicio = 'New York' 
objetivo = 'San Francisco'

camino = buscar_camino_mas_corto(mapa, inicio, objetivo)
print(f"\nCamino más corto desde {inicio} hasta {objetivo}:")
print(" -> ".join(camino))

