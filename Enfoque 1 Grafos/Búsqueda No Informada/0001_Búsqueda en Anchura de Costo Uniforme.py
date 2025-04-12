#La Búsqueda de Costo Uniforme (UCS) es una versión informada de BFS que
#considera el costo de la ruta (p. ej., distancia, tiempo o cualquier peso).
#Siempre expande primero el nodo de menor costo, lo que garantiza el menor
#costo total para el objetivo.

from heapq import heappush, heappop

# Distancias entre ciudades (en millas)
mapa = {
    'Nueva York': [('Filadelfia', 95), ('Boston', 215)],
    'Filadelfia': [('Nueva York', 95), ('Washington D.C.', 123)],
    'Boston': [('Nueva York', 215), ('Chicago', 983)],
    'Washington D.C.': [('Filadelfia', 123), ('Atlanta', 638)],
    'Chicago': [('Boston', 983), ('Denver', 1003)],
    'Atlanta': [('Washington D.C.', 638), ('Miami', 661)],
    'Miami': [('Atlanta', 661)],
    'Denver': [('Chicago', 1003), ('Los Ángeles', 1015)],
    'Los Ángeles': [('Denver', 1015), ('San Francisco', 381)],
    'San Francisco': [('Los Ángeles', 381)]
}

def busqueda_costo_uniforme(mapa, inicio, destino):
    cola = [(0, [inicio])]
    visitados = set()

    while cola:
        costo, camino = heappop(cola)
        ciudad_actual = camino[-1]

        if ciudad_actual in visitados:
            continue
        visitados.add(ciudad_actual)

        if ciudad_actual == destino:
            return camino, costo

        for vecino, costo_ruta in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                nuevo_camino = camino + [vecino]
                nuevo_costo = costo + costo_ruta
                heappush(cola, (nuevo_costo, nuevo_camino))

    return None, float('inf')

# Ejemplo de uso
inicio = 'Nueva York'
destino = 'San Francisco'

camino, costo_total = busqueda_costo_uniforme(mapa, inicio, destino)

print(f"\n Ruta más barata desde '{inicio}' hasta '{destino}':")
print(" -> ".join(camino))
print(f"Distancia total: '{costo_total}' millas")
