## Incertidumbre y Probabilidad es un enfoque que representa el conocimiento incompleto mediante distribuciones de probabilidad, permitiendo inferencias racionales con información parcial.
## f(x) = P(x), donde P representa la probabilidad de que ocurra un evento dado un modelo de incertidumbre.

import random

# Estados del clima
climas = ['Soleado', 'Nublado', 'Lluvioso']

# Distribución de probabilidad inicial
P_clima = {
    'Soleado': 0.6,
    'Nublado': 0.3,
    'Lluvioso': 0.1
}

# Sensores que reportan el clima con su probabilidad de error
P_sensor_dado_clima = {
    'Sensor dice Soleado': {'Soleado': 0.8, 'Nublado': 0.2, 'Lluvioso': 0.1},
    'Sensor dice Nublado': {'Soleado': 0.1, 'Nublado': 0.6, 'Lluvioso': 0.3},
    'Sensor dice Lluvioso': {'Soleado': 0.1, 'Nublado': 0.2, 'Lluvioso': 0.6},
}

evidencia = 'Sensor dice Lluvioso'

def probabilidad_posterior(P_priori, P_likely, evidencia):
    numeradores = {}
    for clima in climas:
        numeradores[clima] = P_likely[evidencia][clima] * P_priori[clima]
    normalizador = sum(numeradores.values())
    return {clima: numeradores[clima] / normalizador for clima in climas}

P_actualizada = probabilidad_posterior(P_clima, P_sensor_dado_clima, evidencia)
print(f"\nDistribución posterior dado que '{evidencia}':")
for clima, prob in P_actualizada.items():
    print(f"P({clima} | evidencia) = {prob:.2f}")
