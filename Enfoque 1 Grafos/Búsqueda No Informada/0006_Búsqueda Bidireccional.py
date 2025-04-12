## La Búsqueda Bidireccional busca simultáneamente desde el origen y el destino.
## Es útil cuando se conoce el objetivo y se quiere acelerar el proceso.
## Reduce la cantidad de nodos explorados en comparación con otras búsquedas.

# Buscador de Archivos
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

def busqueda_bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]


    desde_inicio = {inicio: [inicio]}
    desde_objetivo = {objetivo: [objetivo]}


    frontera_inicio = [inicio]
    frontera_objetivo = [objetivo]

    while frontera_inicio and frontera_objetivo:
        actual_inicio = frontera_inicio.pop(0)
        for vecino in grafo.get(actual_inicio, []):
            if vecino not in desde_inicio:
                nuevo_camino = desde_inicio[actual_inicio] + [vecino]
                desde_inicio[vecino] = nuevo_camino
                frontera_inicio.append(vecino)
                if vecino in desde_objetivo:
                    return nuevo_camino + desde_objetivo[vecino][-2::-1]

    
        actual_objetivo = frontera_objetivo.pop(0)
        for nodo, hijos in grafo.items():
            if actual_objetivo in hijos and nodo not in desde_objetivo:
                nuevo_camino = [nodo] + desde_objetivo[actual_objetivo]
                desde_objetivo[nodo] = nuevo_camino
                frontera_objetivo.append(nodo)
                if nodo in desde_inicio:
                    return desde_inicio[nodo] + desde_objetivo[nodo][-2::-1]

    return None


inicio = '/'
objetivo = 'syslog'

camino = busqueda_bidireccional(archivo_sistema, inicio, objetivo)

# resultado
print(f"\nRuta desde '{inicio}' hasta '{objetivo}':")
print(" -> ".join(camino))

