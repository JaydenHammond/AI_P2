## Q-learning es un algoritmo de Aprendizaje por Refuerzo Activo que aprende una política óptima actualizando los valores Q(s, a) sin necesidad de conocer el modelo completo del entorno.
## f(n) = Q(s, a), donde Q representa el valor esperado de la acción a en el estado s siguiendo una política óptima.

import random

estados = ['A', 'B', 'C', 'Terminal']
acciones = ['derecha', 'abajo']

# (Estado, accion) -> (siguiente_estado, recompensa)
modelo = {
    ('A', 'derecha'): ('B', -1),
    ('B', 'derecha'): ('C', -1),
    ('C', 'abajo'):   ('Terminal', 10)
}

# Inicializar Q(s, a)
Q = {(s, a): 0 for s in estados for a in acciones}

# Parametros Q-learning
alpha = 0.5
gamma = 0.9
epsilon = 0.2

def acciones_validas(estado):
    return [a for (s, a) in modelo if s == estado]

def elegir_accion(estado):
    if random.random() < epsilon:
        return random.choice(acciones_validas(estado))
    return max(acciones_validas(estado), key=lambda a: Q[(estado, a)])

for episodio in range(100):
    estado = 'A'
    while estado != 'Terminal':
        accion = elegir_accion(estado)
        siguiente_estado, recompensa = modelo.get((estado, accion), (estado, -10))  # Penaliza si acción no válida
        acciones_siguiente = acciones_validas(siguiente_estado)
        mejor_q = max([Q.get((siguiente_estado, a), 0) for a in acciones_siguiente] or [0])
        
        # Regla de  Q-learning
        Q[(estado, accion)] += alpha * (recompensa + gamma * mejor_q - Q[(estado, accion)])
        
        estado = siguiente_estado


politica = {}
for estado in estados:
    if estado == 'Terminal': continue
    posibles = acciones_validas(estado)
    if posibles:
        mejor = max(posibles, key=lambda a: Q[(estado, a)])
        politica[estado] = mejor

print("\nPolítica óptima aprendida con Q-learning:")
for estado, accion in politica.items():
    print(f"{estado} → {accion}")
