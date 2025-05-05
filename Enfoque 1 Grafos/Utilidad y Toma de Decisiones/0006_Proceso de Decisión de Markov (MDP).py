## Proceso de Decisión de Markov (MDP) modela decisiones secuenciales donde el resultado depende del estado actual y la acción, bajo incertidumbre.
## f(n) = (S, A, T, R, γ), donde se calcula una política que maximiza las recompensas esperadas a largo plazo.

# Definición del MDP
estados = ['Inicio', 'A', 'B', 'Meta']
acciones = ['Ir_A', 'Ir_B', 'Terminar']

# Transiciones: (estado, acción) -> [(probabilidad, siguiente_estado, recompensa)]
transiciones = {
    'Inicio': {
        'Ir_A': [(1.0, 'A', 0)],
        'Ir_B': [(1.0, 'B', 0)]
    },
    'A': {
        'Terminar': [(1.0, 'Meta', 10)]
    },
    'B': {
        'Terminar': [(1.0, 'Meta', 5)]
    },
    'Meta': {}
}

# Parámetros del MDP
gamma = 0.9  # Factor de descuento

# Inicializar valores
V = {s: 0 for s in estados}

def resolver_mdp(estados, acciones, transiciones, gamma, theta=0.001):
    """Resuelve el MDP con iteración de valores."""
    V = {s: 0 for s in estados}
    politica = {s: None for s in estados}

    while True:
        delta = 0
        for s in estados:
            if not transiciones.get(s):
                continue
            v_actual = V[s]
            valores_acciones = {}
            for a in transiciones[s]:
                valores_acciones[a] = sum(p * (r + gamma * V[s_next]) for p, s_next, r in transiciones[s][a])
            mejor_accion = max(valores_acciones, key=valores_acciones.get)
            V[s] = valores_acciones[mejor_accion]
            politica[s] = mejor_accion
            delta = max(delta, abs(v_actual - V[s]))
        if delta < theta:
            break
    return politica, V
politica_optima, valores = resolver_mdp(estados, acciones, transiciones, gamma)

print("\nPolítica óptima (Proceso de Decisión de Markov):")
for estado in estados:
    accion = politica_optima.get(estado)
    print(f"{estado}: {accion if accion else '—'}")
print("\nValores de utilidad por estado:")
for estado, valor in valores.items():
    print(f"{estado}: {valor:.3f}")
