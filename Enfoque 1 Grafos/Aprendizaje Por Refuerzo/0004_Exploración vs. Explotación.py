## Exploración vs. Explotación es una estrategia fundamental en Aprendizaje por Refuerzo que equilibra la elección entre probar nuevas acciones (explorar) y aprovechar las ya conocidas (explotar).
## f(n) = ε, donde ε representa la probabilidad de tomar una acción aleatoria en lugar de la mejor conocida.

import random

estados = ['Inicio', 'Meta']
acciones = ['izquierda', 'derecha']

#(Estado, acción) -> (siguiente_estado, recompensa)
modelo = {
    ('Inicio', 'izquierda'): ('Inicio', -1),
    ('Inicio', 'derecha'): ('Meta', 10),
}

# Inicialización de Qvalores
Q = {(s, a): 0 for s in estados for a in acciones}

# Parámetros
alpha = 0.5
gamma = 0.9

tasas_exploracion = [0.0, 0.1, 0.5, 1.0]
for epsilon in tasas_exploracion:
    Q = {(s, a): 0 for s in estados for a in acciones}

    for episodio in range(50):
        estado = 'Inicio'
        while estado != 'Meta':
            if random.random() < epsilon:
                accion = random.choice(acciones)
            else:
                accion = max(acciones, key=lambda a: Q[(estado, a)])
            
            siguiente_estado, recompensa = modelo.get((estado, accion), (estado, -5))
            mejor_q = max(Q[(siguiente_estado, a)] for a in acciones)
            Q[(estado, accion)] += alpha * (recompensa + gamma * mejor_q - Q[(estado, accion)])
            estado = siguiente_estado

    print(f"\nPolítica aprendida con ε = {epsilon}:")
    for estado in estados:
        if estado == 'Meta':
            continue
        mejor_accion = max(acciones, key=lambda a: Q[(estado, a)])
        print(f"{estado} → {mejor_accion}")
