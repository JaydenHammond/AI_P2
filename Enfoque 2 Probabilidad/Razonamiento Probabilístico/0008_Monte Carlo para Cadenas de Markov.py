## Monte Carlo para Cadenas de Markov simula muchas trayectorias para estimar la distribución estacionaria de estados.
## f(n) = tras N pasos, la fracción de visitas a cada estado aproxima P(estacionaria).

import random

# RECORDATORIO: defino los estados de la cadena de Markov.
estados = ['S1', 'S2', 'S3']

# RECORDATORIO: matriz de transición P(next | current).
# Cada fila suma 1.0. Por ejemplo, de S1 va a S1 con 0.1, S2 con 0.6, S3 con 0.3.
P = {
    'S1': {'S1': 0.1, 'S2': 0.6, 'S3': 0.3},
    'S2': {'S1': 0.4, 'S2': 0.2, 'S3': 0.4},
    'S3': {'S1': 0.3, 'S2': 0.3, 'S3': 0.4},
}

# RECORDATORIO: función para muestrear el siguiente estado dado el actual.
def siguiente_estado(estado_actual):
    r = random.random()  # RECORDATORIO: u ~ Uniforme[0,1)
    acumulado = 0.0
    for est, prob in P[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            return est
    return estado_actual  # RECORDATORIO: por seguridad, retorno el actual si hay redondeo

# RECORDATORIO: simulación Monte Carlo.
def simular_cadena(paso_inicial, N):
    visitas = {s: 0 for s in estados}  # contador de visitas a cada estado
    estado = paso_inicial
    for _ in range(N):
        estado = siguiente_estado(estado)
        visitas[estado] += 1
    return visitas

# RECORDATORIO: número de pasos grandes para aproximar la estacionaria.
N = 100000
# RECORDATORIO: elijo un estado inicial arbitrario, por ejemplo S1.
visitas = simular_cadena('S1', N)

# RECORDATORIO: convierto conteos a frecuencias (estimación de distribución estacionaria).
dist_estacionaria = {s: visitas[s] / N for s in estados}

# RESULTADO: muestro la distribución estacionaria estimada.
print("\nEstimación de distribución estacionaria tras Monte Carlo:")
for s, prob in dist_estacionaria.items():
    print(f"P_est({s}) ≈ {prob:.3f}")
