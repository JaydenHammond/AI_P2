## Aprendizaje por Refuerzo Activo permite al agente aprender la mejor política explorando el entorno y actualizando los valores de acción (Q-valores) con base en la experiencia.
## f(n) = Q(s, a), donde Q representa la utilidad esperada de tomar acción a en estado s y seguir una política óptima después.

import random

# Estados y acciones posibles
estados = ['A', 'B', 'C', 'Terminal']
acciones = ['derecha', 'abajo']

# (Estado, acción) -> (siguiente_estado, recompensa)
modelo = {
    ('A', 'derecha'): ('B', -1),
    ('B', 'derecha'): ('C', -1),
    ('C', 'abajo'): ('Terminal', 10)
}

# Inicialización Q(s, a) = 0
Q = {(s, a): 0 for s in estados for a in acciones}

# Parámetros
alpha = 0.5
gamma = 0.9
epsilon = 0.2

def acciones_validas(estado):
    return [a for (s, a) in modelo if s == estado]

def elegir_accion(estado):
    if random.random() < epsilon:
        return random.choice(acciones_validas(estado))
    else:
        return max(acciones_validas(estado), key=lambda a: Q[(estado, a)])

for episodio in range(100):
    estado = 'A'
    while estado != 'Terminal':
        accion = elegir_accion(estado)
        siguiente_estado, recompensa = modelo.get((estado, accion), (estado, -10))  # Penaliza acciones inválidas
        mejor_q = max([Q.get((siguiente_estado, a), 0) for a in acciones_validas(siguiente_estado)] or [0])
        Q[(estado, accion)] += alpha * (recompensa + gamma * mejor_q - Q[(estado, accion)])
        estado = siguiente_estado  # ← Corrección aquí

politica_optima = {}
for estado in estados:
    if estado == 'Terminal': continue
    mejores = acciones_validas(estado)
    if mejores:
        politica_optima[estado] = max(mejores, key=lambda a: Q[(estado, a)])

print("\nPolítica aprendida por refuerzo activo (Q-learning):")
for estado, accion in politica_optima.items():
    print(f"{estado} → {accion}")
