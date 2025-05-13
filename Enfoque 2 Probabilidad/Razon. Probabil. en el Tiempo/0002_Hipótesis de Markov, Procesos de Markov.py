## Procesos de Markov modelan secuencias de variables donde el futuro depende solo del estado presente (Hipótesis de Markov).
## f(Xₜ₊₁ | Xₜ) = Pₓ[Xₜ → Xₜ₊₁], representado por una matriz de transición.

import random

# RECORDATORIO: Defino los estados del proceso, por ejemplo distintos climas.
estados = ['Soleado', 'Nublado', 'Lluvioso']

# RECORDATORIO: Matriz de transición P(next | current), cada fila suma 1.
P = {
    'Soleado': {'Soleado': 0.7, 'Nublado': 0.2, 'Lluvioso': 0.1},
    'Nublado': {'Soleado': 0.3, 'Nublado': 0.4, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.2, 'Nublado': 0.3, 'Lluvioso': 0.5},
}

# RECORDATORIO: Distribución inicial P(X₀)
dist_inicial = {'Soleado': 0.5, 'Nublado': 0.3, 'Lluvioso': 0.2}

# RECORDATORIO: Función para muestrear el siguiente estado dado el estado actual.
def siguiente_estado(estado_actual):
    r = random.random()  # valor uniforme [0,1)
    acumulado = 0.0
    for est, prob in P[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            return est
    return estado_actual  # por seguridad si hay redondeos

# RECORDATORIO: Muestreo inicial de X₀ según dist_inicial
def muestrear_inicial():
    r = random.random()
    acumulado = 0.0
    for est, prob in dist_inicial.items():
        acumulado += prob
        if r < acumulado:
            return est
    return list(dist_inicial.keys())[-1]

# RECORDATORIO: Simulo la cadena de Markov durante T pasos.
def simular_markov(T):
    cadena = []
    estado = muestrear_inicial()
    cadena.append(estado)
    for _ in range(1, T):
        estado = siguiente_estado(estado)
        cadena.append(estado)
    return cadena

# RECORDATORIO: Corro la simulación y muestro los primeros pasos.
T = 20
trayectoria = simular_markov(T)

print("\nSimulación de Procesos de Markov (Hipótesis de Markov):")
for t, est in enumerate(trayectoria):
    print(f"Paso {t}: {est}")
