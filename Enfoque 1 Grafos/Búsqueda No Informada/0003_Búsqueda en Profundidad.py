# Búsqueda No Informada - Búsqueda en Profundidad (DFS)
# Este algoritmo explora un grafo avanzando lo más lejos posible por cada rama
# antes de retroceder (backtracking).

# Ciudades de estados Unidos
mapa = {
    'Nueva York': ['Filadelfia', 'Boston'],
    'Filadelfia': ['Nueva York', 'Washington D.C.'],
    'Boston': ['Nueva York', 'Chicago'],
    'Washington D.C.': ['Filadelfia', 'Atlanta'],
    'Chicago': ['Boston', 'Denver'],
    'Atlanta': ['Washington D.C.', 'Miami'],
    'Miami': ['Atlanta'],
    'Denver': ['Chicago', 'Los Ángeles'],
    'Los Ángeles': ['Denver', 'San Francisco'],
    'San Francisco': ['Los Ángeles']
}

def busqueda_profundidad(mapa, inicio, destino):
    pila = [(inicio, [inicio])]
    visitados = set()
    
    while pila:
        nodo_actual, camino = pila.pop()
        
        if nodo_actual == destino:
            return camino
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            for vecino in reversed(mapa.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
    
    return None

inicio = 'Nueva York'
destino = 'San Francisco'

print(f"Buscando ruta desde {inicio} hasta {destino}:")
camino = busqueda_profundidad(mapa, inicio, destino)
print(" -> ".join(camino))
