##La Búsqueda en Profundidad Iterativa combina lo mejor de:
##La Búsqueda en Profundidad, que usa poca memoria.
##La Búsqueda en Anchura, que garantiza encontrar el camino más corto (en cantidad de pasos).
##Explora el grafo por niveles, como una serie de búsquedas en profundidad con límite creciente.

# Buscardor de Archivos
archivo_sistema = {
    '/': ['Desktop', 'var'],
    'Desktop': ['Jayden'],
    'Jayden': ['docs', 'pics'],
    'docs': ['AiNotes.txt'],
    'pics': ['Dickpick.jpg'],
    'var': ['log'],
    'log': ['syslog'],
    'AiNotes.txt': [],
    'Dickpick.jpg': [],
    'syslog': []
}

def busqueda_profundidad_iterativa(grafo, inicio, objetivo, profundidad_maxima):
    for limite in range(1, profundidad_maxima + 1):
        print(f"Buscando con límite de profundidad: {limite}")
        resultado = dfs_limitado(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None

def dfs_limitado(grafo, nodo, objetivo, limite):
    pila = [(nodo, [nodo], 0)]
    while pila:
        actual, camino, profundidad = pila.pop()

        if actual == objetivo:
            return camino

        if profundidad < limite:
            for vecino in grafo.get(actual, []):
                nuevo_camino = camino + [vecino]
                pila.append((vecino, nuevo_camino, profundidad + 1))

    return None

#Resultados
inicio = '/'
objetivo = 'syslog'
profundidad_maxima = 5

camino_encontrado = busqueda_profundidad_iterativa(archivo_sistema, inicio, objetivo, profundidad_maxima)

print(f"\nRuta en '{objetivo}':")
print(" -> ".join(camino_encontrado))

