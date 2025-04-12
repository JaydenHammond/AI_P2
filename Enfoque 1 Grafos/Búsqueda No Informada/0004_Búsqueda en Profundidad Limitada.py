# Búsqueda No Informada - Búsqueda en Profundidad Limitada (DLS)
# Este algoritmo explora un grafo hasta una profundidad máxima dada,
# evitando ciclos infinitos en grafos muy grandes.

# Ciudades de Estados Unidos
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

def busqueda_profundidad_limitada(mapa, inicio, destino, limite_profundidad):
    pila = [(inicio, [inicio], 0)]
    visitados = set()
    
    while pila:
        nodo_actual, camino, profundidad = pila.pop()
        
        if nodo_actual == destino:
            return camino
        

        if profundidad < limite_profundidad and nodo_actual not in visitados:
            visitados.add(nodo_actual)
            

            for vecino in reversed(mapa.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino], profundidad + 1))
    
    return None


inicio = 'Nueva York'
destino = 'San Francisco'
limite_profundidad = 5 

print(f"Buscando ruta desde {inicio} hasta {destino} con profundidad máxima {limite_profundidad}:")
camino = busqueda_profundidad_limitada(mapa, inicio, destino, limite_profundidad)
print("Ruta encontrada:")
print(" → ".join(camino))


