## Iteración de Valores es un algoritmo de programación dinámica que actualiza los valores de cada estado hasta converger a una política óptima.
## f(n) = max_a ∑ P(s'|s,a) × [R(s,a,s') + γ × V(s')]; mejora la política evaluando acciones que maximizan recompensa futura.

# Estados posibles (habitaciones de un robot aspiradora)
estados = ['A', 'B']

# Acciones disponibles en cada estado
acciones = ['Limpiar', 'Mover']

# Transiciones y recompensas: (estado, acción) -> [(probabilidad, siguiente_estado, recompensa)]
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

# Parámetros
gamma = 0.9          # Factor de descuento
theta = 0.001        # Umbral de convergencia

# Inicialización de valores
V = {s: 0 for s in estados}

def iteracion_valores(estados, acciones, transiciones, gamma, theta):
    """Aplica iteración de valores para encontrar los valores óptimos."""
    V = {s: 0 for s in estados}
    while True:
        delta = 0
        for s in estados:
            v_actual = V[s]
            valores_accion = []
            for a in acciones:
                suma = 0
                for prob, s_next, recompensa in transiciones[s].get(a, []):
                    suma += prob * (recompensa + gamma * V[s_next])
                valores_accion.append(suma)
            V[s] = max(valores_accion)
            delta = max(delta, abs(v_actual - V[s]))
        if delta < theta:
            break
    return V
valores_finales = iteracion_valores(estados, acciones, transiciones, gamma, theta)

print("\nValores óptimos por estado (Iteración de Valores):")
for estado, valor in valores_finales.items():
    print(f"Estado {estado}: {valor:.3f}")
