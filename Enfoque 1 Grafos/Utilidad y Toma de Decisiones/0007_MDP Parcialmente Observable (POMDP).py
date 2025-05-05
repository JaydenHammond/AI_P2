## MDP Parcialmente Observable (POMDP) extiende el MDP clásico permitiendo decisiones basadas en creencias sobre el estado actual en vez del estado real.
## f(n) = (S, A, T, R, Ω, O, γ), donde se elige la acción que maximiza la recompensa esperada sobre la creencia actual del agente.

import random

# Estados posibles
estados = ['Bueno', 'Malo']

# Acciones disponibles
acciones = ['Revisar', 'Actuar']

# Observaciones posibles
observaciones = ['Parece Bueno', 'Parece Malo']

# Función de transición T[s][a] = [(prob, siguiente_estado, recompensa)]
transiciones = {
    'Bueno': {
        'Revisar': [(1.0, 'Bueno', -1)],
        'Actuar': [(1.0, 'Bueno', 10)],
    },
    'Malo': {
        'Revisar': [(1.0, 'Malo', -1)],
        'Actuar': [(1.0, 'Malo', -10)],
    }
}

# Modelo de observación: O[a][s'][o] = probabilidad de observar 'o' si el estado real es s' y se ejecutó a
observaciones_modelo = {
    'Revisar': {
        'Bueno': {'Parece Bueno': 0.8, 'Parece Malo': 0.2},
        'Malo':  {'Parece Bueno': 0.3, 'Parece Malo': 0.7}
    },
    'Actuar': {
        'Bueno': {'Parece Bueno': 0.5, 'Parece Malo': 0.5},
        'Malo':  {'Parece Bueno': 0.5, 'Parece Malo': 0.5}
    }
}
gamma = 0.9

# Creencia inicial (probabilidad de que el estado sea 'Bueno' o 'Malo')
creencia = {'Bueno': 0.5, 'Malo': 0.5}

def actualizar_creencia(creencia, accion, observacion):
    """Actualiza la creencia usando la observación y la acción tomada."""
    nueva = {}
    total = 0
    for s in estados:
        prob_o_dado_s = observaciones_modelo[accion][s][observacion]
        nueva[s] = prob_o_dado_s * creencia[s]
        total += nueva[s]
    for s in nueva:
        nueva[s] /= total
    return nueva

def recompensa_esperada(creencia, accion):
    """Calcula la recompensa esperada tomando una acción bajo una creencia."""
    recompensa = 0
    for s in estados:
        trans = transiciones[s][accion]
        recompensa += creencia[s] * sum(p * r for p, _, r in trans)
    return recompensa

accion = 'Revisar'
observacion = 'Parece Malo'
creencia = actualizar_creencia(creencia, accion, observacion)
mejor_accion = max(acciones, key=lambda a: recompensa_esperada(creencia, a))

print("\nCreencia actual tras observar '{}':".format(observacion))
for estado, prob in creencia.items():
    print(f"{estado}: {prob:.2f}")

print(f"\nMejor acción según creencia actual: {mejor_accion}")
