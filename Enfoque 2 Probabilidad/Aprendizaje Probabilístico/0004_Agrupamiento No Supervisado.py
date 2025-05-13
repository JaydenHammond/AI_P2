## Agrupamiento No Supervisado usa K-means para particionar datos en k grupos basados en distancia.
## f(C) = ∑‖x − μ_{cluster(x)}‖²; iteramos asignación y actualización de centroides.

import random
import math

# RECORDATORIO: datos de ejemplo: puntos en 2D.
datos = [
    (1.0, 2.0), (1.5, 1.8), (5.0, 8.0),
    (8.0, 8.0), (1.0, 0.6), (9.0, 11.0),
    (8.0, 2.0), (10.0, 2.0), (9.0, 3.0)
]

# RECORDATORIO: número de clusters deseados.
k = 3

# RECORDATORIO: inicializo centroides eligiendo k puntos aleatorios.
centroides = random.sample(datos, k)

# RECORDATORIO: función para calcular la distancia euclidiana.
def distancia(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

# RECORDATORIO: algoritmo principal de K-means.
def k_means(datos, centroides, max_iter=10):
    for it in range(max_iter):
        # 1) Asignación de puntos al cluster más cercano
        clusters = {i: [] for i in range(len(centroides))}
        for x in datos:
            # RECORDATORIO: elijo el índice de centrod más cercano
            distancias = [distancia(x, c) for c in centroides]
            idx = distancias.index(min(distancias))
            clusters[idx].append(x)
        # 2) Actualización de centroides como promedio de cada cluster
        nuevos = []
        for i in range(len(centroides)):
            pts = clusters[i]
            if pts:
                # RECORDATORIO: promedio de coordenadas x e y
                avg_x = sum(p[0] for p in pts) / len(pts)
                avg_y = sum(p[1] for p in pts) / len(pts)
                nuevos.append((avg_x, avg_y))
            else:
                # RECORDATORIO: si cluster vacío, no muevo el centroide
                nuevos.append(centroides[i])
        # RECORDATORIO: chequeo convergencia
        if all(distancia(centroides[i], nuevos[i]) < 1e-4 for i in range(k)):
            break
        centroides[:] = nuevos
    return clusters, centroides

clusters, centroides_finales = k_means(datos, centroides)

print("Centroides finales:")
for c in centroides_finales:
    print(f"  {c}")

print("\nPuntos por cluster:")
for idx, pts in clusters.items():
    print(f"Cluster {idx}: {pts}")
