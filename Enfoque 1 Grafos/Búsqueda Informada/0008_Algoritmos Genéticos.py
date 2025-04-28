## Algoritmo Genético es una búsqueda informada que simula el proceso de evolución natural para encontrar soluciones óptimas o cercanas al óptimo.
## f(n) = h(n), donde h es la evaluación de la calidad de una solución; utiliza selección, cruce y mutación para explorar el espacio de soluciones.

import random

# Grafo DND
mazmorra = {
    'Entrada': [('Sala1', 3), ('Sala2', 5)],
    'Sala1': [('Tesoro', 7)],
    'Sala2': [('Sala3', 2)],
    'Sala3': [('Tesoro', 4)],
    'Tesoro': []
}

# Heurística: distancia estimada al Tesoro
heuristica = {
    'Entrada': 10,
    'Sala1': 7,
    'Sala2': 6,
    'Sala3': 3,
    'Tesoro': 0
}

def algoritmo_genetico(grafo, heuristica, inicio, objetivo, poblacion_size=10, generaciones=100, probabilidad_cruce=0.7, probabilidad_mutacion=0.1):
    def generar_individuo():
        camino = [inicio]
        while camino[-1] != objetivo:
            vecinos = grafo.get(camino[-1], [])
            if not vecinos:
                break
            camino.append(random.choice(vecinos)[0])
        return camino
    
    def evaluar(individuo):
        return heuristica.get(individuo[-1], float('inf'))
    
    def cruzar(padre1, padre2):
        punto_cruce = random.randint(1, min(len(padre1), len(padre2)) - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        return hijo1, hijo2
    
    def mutar(individuo):
        if random.random() < probabilidad_mutacion:
            indice_mutacion = random.randint(0, len(individuo) - 1)
            vecinos = grafo.get(individuo[indice_mutacion], [])
            if vecinos:
                individuo[indice_mutacion] = random.choice(vecinos)[0]
        return individuo

    poblacion = [generar_individuo() for _ in range(poblacion_size)]

    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=lambda x: evaluar(x))
        if poblacion[0][-1] == objetivo:
            return poblacion[0]
        padres = poblacion[:poblacion_size // 2]

        nueva_poblacion = []
        for i in range(0, len(padres), 2):
            if random.random() < probabilidad_cruce:
                hijo1, hijo2 = cruzar(padres[i], padres[i+1])
                nueva_poblacion.extend([hijo1, hijo2])
            else:
                nueva_poblacion.extend([padres[i], padres[i+1]])
        nueva_poblacion = [mutar(ind) for ind in nueva_poblacion]
        poblacion = nueva_poblacion[:poblacion_size]

    return None

# Objetivo
inicio = 'Entrada'
objetivo = 'Tesoro'

camino = algoritmo_genetico(mazmorra, heuristica, inicio, objetivo)

print(f"\nRuta tentativa desde '{inicio}' hasta '{objetivo}' usando Algoritmo Genético:")
print(" -> ".join(camino))
