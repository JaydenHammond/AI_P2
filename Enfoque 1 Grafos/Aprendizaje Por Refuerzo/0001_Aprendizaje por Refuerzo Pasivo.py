## Aprendizaje por Refuerzo Pasivo evalúa una política fija observando episodios y estimando los valores de los estados visitados.
## f(n) = V(s), donde V(s) es el valor estimado del estado s bajo la política observada.

import random

# Estado
estados = ['A', 'B', 'C', 'Terminal']

# Política
politica = {
    'A': 'derecha',
    'B': 'derecha',
    'C': 'abajo'
}

# Modelo de transición determinista:
modelo = {
    ('A', 'derecha'): ('B', -1),
    ('B', 'derecha'): ('C', -1),
    ('C', 'abajo'): ('Terminal', 10)
}

# Inicializar V(s) = 0
valores = {estado: 0 for estado in estados}
conteo = {estado: 0 for estado in estados}
def ejecutar_episodio():
    estado = 'A'
    trayectoria = []
    while estado != 'Terminal':
        accion = politica[estado]
        siguiente_estado, recompensa = modelo[(estado, accion)]
        trayectoria.append((estado, recompensa))
        estado = siguiente_estado
    return trayectoria

for episodio in range(100):
    episodio_data = ejecutar_episodio()
    total_recompensa = 0
    for estado, recompensa in reversed(episodio_data):
        total_recompensa = recompensa + total_recompensa
        conteo[estado] += 1
        valores[estado] += (total_recompensa - valores[estado]) / conteo[estado]

print("\nValores estimados de los estados bajo la política fija:")
for estado in estados:
    print(f"{estado}: {valores[estado]:.2f}")
