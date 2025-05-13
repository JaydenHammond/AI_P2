## k-NN, k-Medias y Clustering: tres métodos fundamentales para clasificación y agrupamiento de datos.
## k-NN clasifica nuevos puntos por mayoría de vecinos; k-Medias agrupa datos en k clusters iterativamente; Clustering simple conecta puntos cercanos.

import random
import math

# RECORDATORIO: función para calcular distancia Euclidiana en 2D
def distancia(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

# RECORDATORIO: k-NN predice la clase de 'pt' usando los k vecinos más cercanos
def knn(datos, pt, k=3):
    # datos: lista de (punto, etiqueta)
    # RECORDATORIO: ordeno por distancia y tomo las k más pequeñas
    vecinos = sorted(datos, key=lambda x: distancia(x[0], pt))[:k]
    # RECORDATORIO: voto mayoritario
    votos = {}
    for _, etiqueta in vecinos:
        votos[etiqueta] = votos.get(etiqueta, 0) + 1
    # RECORDATORIO: devuelvo etiqueta con más votos
    return max(votos, key=votos.get)

# EJEMPLO k-NN
datos_clasif = [((1,2),'A'), ((2,1),'A'), ((8,9),'B'), ((9,8),'B')]
nuevo = (3,3)
print("k-NN → etiqueta de", nuevo, "=", knn(datos_clasif, nuevo, k=3))

# RECORDATORIO: inicializo centroides tomando k puntos aleatorios
def k_means(datos, k=2, iters=10):
    # datos: lista de puntos 2D
    centroides = random.sample(datos, k)
    for _ in range(iters):
        clusters = {i: [] for i in range(k)}
        # asignación
        for x in datos:
            idx = min(range(k), key=lambda i: distancia(x, centroides[i]))
            clusters[idx].append(x)
        # actualización
        nuevos = []
        for i in range(k):
            pts = clusters[i]
            if pts:
                avg_x = sum(p[0] for p in pts)/len(pts)
                avg_y = sum(p[1] for p in pts)/len(pts)
                nuevos.append((avg_x, avg_y))
            else:
                nuevos.append(centroides[i])
        centroides = nuevos
    return clusters, centroides

# EJEMPLO k-Medias
datos_cluster = [(1,1),(2,2),(1,2),(8,8),(9,9),(8,9)]
clusters, cent = k_means(datos_cluster, k=2)
print("\nk-Medias → centroides:", cent)
for i, pts in clusters.items():
    print(f" Cluster {i}:", pts)

# RECORDATORIO: agrupa puntos que estén a menos de 'umbral' de distancia formando componentes conectadas
def clustering_conectividad(datos, umbral=3.0):
    n = len(datos)
    vistos = [False]*n
    grupos = []
    for i in range(n):
        if vistos[i]: continue
        # BFS para componente
        cola, comp = [i], []
        vistos[i] = True
        while cola:
            u = cola.pop()
            comp.append(datos[u])
            for v in range(n):
                if not vistos[v] and distancia(datos[u], datos[v]) <= umbral:
                    vistos[v] = True
                    cola.append(v)
        grupos.append(comp)
    return grupos

# EJEMPLO Clustering Simple
datos_con = [(1,1),(2,1),(5,5),(5,6),(9,9)]
grupos = clustering_conectividad(datos_con, umbral=1.5)
print("\nClustering Conectividad → grupos:")
for g in grupos:
    print(" ", g)
