## Búsqueda de la Política es un método de optimización que ajusta directamente los parámetros de una política para maximizar la recompensa esperada.
## f(π) = E[recompensa total], donde π es la política que se actualiza iterativamente buscando mejores acciones en cada estado.

import random

estados = ['S1', 'S2']
acciones = ['a1', 'a2']

#(Estado, acción) -> (siguiente_estado, recompensa)
modelo = {
    ('S1', 'a1'): ('S1', 2),
    ('S1', 'a2'): ('S2', 0),
    ('S2', 'a1'): ('S1', 1),
    ('S2', 'a2'): ('S2', 3),
}

politica = {s: random.choice(acciones) for s in estados}

def evaluar_politica(politica, gamma=0.9, iteraciones=10):
    V = {s: 0 for s in estados}
    for _ in range(iteraciones):
        for s in estados:
            a = politica[s]
            s_next, r = modelo[(s, a)]
            V[s] = r + gamma * V[s_next]
    return V

def mejorar_politica(V, gamma=0.9):
    nueva_politica = {}
    for s in estados:
        mejor_accion = max(acciones, key=lambda a: modelo[(s, a)][1] + gamma * V[modelo[(s, a)][0]])
        nueva_politica[s] = mejor_accion
    return nueva_politica
for paso in range(5):
    V = evaluar_politica(politica)
    politica = mejorar_politica(V)

print("Política optimizada:")
for estado in estados:
    print(f"{estado} → {politica[estado]}")
