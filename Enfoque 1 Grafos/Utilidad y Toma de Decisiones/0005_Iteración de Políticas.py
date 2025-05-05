## Iteración de Políticas alterna entre evaluación y mejora de una política hasta que converge en la política óptima.
## f(n) = evalúa Vπ(s) con π(s) y luego mejora π(s) := argmax_a ∑ P(s'|s,a) × [R + γV(s')]; repite hasta estabilización.

# Estados posibles (habitaciones)
estados = ['A', 'B']

# Acciones posibles
acciones = ['Limpiar', 'Mover']

# Transiciones y recompensas: (estado, acción) -> [(prob, siguiente_estado, recompensa)]
transiciones = {
    'A': {
        'Limpiar': [(1.0, 'A', 1)],
        'Mover': [(1.0, 'B', 0)]
    },
    'B': {
        'Limpiar': [(1.0, 'B', 2)],
        'Mover': [(1.0, 'A', 0)]
    }
}

# Informacion
gamma = 0.9
theta = 0.001

V = {s: 0 for s in estados}
politica = {s: 'Limpiar' for s in estados}

def evaluar_politica(politica, V, gamma, theta):
    """Evalúa la utilidad de cada estado bajo la política actual."""
    while True:
        delta = 0
        for s in estados:
            v = V[s]
            accion = politica[s]
            V[s] = sum(p * (r + gamma * V[s_next]) for p, s_next, r in transiciones[s][accion])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def mejorar_politica(V, politica, gamma):
    """Mejora la política eligiendo la mejor acción en cada estado."""
    estable = True
    for s in estados:
        accion_actual = politica[s]
        mejores = {}
        for a in acciones:
            mejores[a] = sum(p * (r + gamma * V[s_next]) for p, s_next, r in transiciones[s][a])
        mejor_accion = max(mejores, key=mejores.get)
        if mejor_accion != accion_actual:
            politica[s] = mejor_accion
            estable = False
    return politica, estable

def iteracion_politicas(estados, acciones, transiciones, gamma, theta):
    """Ejecuta el ciclo de evaluación y mejora de políticas."""
    V = {s: 0 for s in estados}
    politica = {s: random.choice(acciones) for s in estados}

    while True:
        V = evaluar_politica(politica, V, gamma, theta)
        politica, estable = mejorar_politica(V, politica, gamma)
        if estable:
            break
    return politica, V
politica_optima, V_optimo = iteracion_politicas(estados, acciones, transiciones, gamma, theta)

print("\nPolítica óptima (Iteración de Políticas):")
for estado in estados:
    print(f"Estado {estado}: Acción -> {politica_optima[estado]}")

print("\nValores por estado:")
for estado, valor in V_optimo.items():
    print(f"{estado}: {valor:.3f}")
