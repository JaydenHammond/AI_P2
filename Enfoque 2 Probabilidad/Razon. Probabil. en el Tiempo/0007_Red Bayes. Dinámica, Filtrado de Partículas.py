## Filtrado de Partículas aplica muestreo secuencial para estimar la creencia en un POMDP sin necesidad de normalizar cada paso.
## f(belief) ≈ conjunto de partículas; se actualiza con muestreo de transición, peso por evidencia y remuestreo.

import random

# RECORDATORIO: defino el espacio de estados ocultos, por ejemplo, posición en 1D: 0, 1, 2.
estados = [0, 1, 2]

# RECORDATORIO: modelo de transición simple: puede quedarse o moverse ±1 (con bordes).
def transicionar(s):
    opciones = [s]
    if s > 0:       opciones.append(s-1)
    if s < 2:       opciones.append(s+1)
    # RECORDATORIO: asigno probabilidades iguales
    return random.choice(opciones)

# RECORDATORIO: modelo de observación: sensor que mide distancia al estado “2” con ruido.
def peso_particula(s, observacion):
    # RECORDATORIO: más cerca de 2 → mayor probabilidad
    dist = abs(s - 2)
    # RECORDATORIO: uso función simple de peso: exp(-dist)
    return 1.0 / (1 + dist)

# RECORDATORIO: inicializo N partículas uniformemente
def inicializar_particulas(N):
    return [random.choice(estados) for _ in range(N)]

# RECORDATORIO: paso de filtrado de partículas
def filtrar_particulas(particulas, observacion):
    # 1) Predicción: aplico transición a cada partícula
    predichas = [transicionar(s) for s in particulas]
    # 2) Ponderación: calculo pesos según la observación
    pesos = [peso_particula(s, observacion) for s in predichas]
    # RECORDATORIO: normalizar pesos
    total = sum(pesos) or 1
    pesos = [p/total for p in pesos]
    # 3) Remuestreo: elijo N partículas según pesos
    nuevas = random.choices(predichas, weights=pesos, k=len(predichas))
    return nuevas

N = 100       # RECORDATORIO: número de partículas
particulas = inicializar_particulas(N)

# Secuencia de observaciones (por ejemplo, mediciones de cercanía al 2)
observaciones = [0.2, 1.0, 0.5, 0.0]  # valores arbitrarios

for t, obs in enumerate(observaciones, 1):
    # RECORDATORIO: cada obs simula “qué tan cerca” se siente del 2
    particulas = filtrar_particulas(particulas, obs)
    # RECORDATORIO: estimación = moda de las partículas
    estima = max(set(particulas), key=particulas.count)
    print(f"Paso {t}: estimación de estado ≈ {estima}")
