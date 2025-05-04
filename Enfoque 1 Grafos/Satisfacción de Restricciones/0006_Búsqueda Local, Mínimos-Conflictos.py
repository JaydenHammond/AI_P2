## Mínimos-Conflictos es una búsqueda local que parte de una solución completa y realiza cambios mínimos para reducir la cantidad de conflictos hasta encontrar una solución válida.
## f(n) = número de conflictos; busca asignaciones que minimicen conflictos en cada iteración hasta llegar a 0.

import random

# Tareas y alumnos
tareas  = ['Tarea A', 'Tarea B', 'Tarea C']
alumnos = ['Alumno 1', 'Alumno 2', 'Alumno 3']

# Fortalezas de cada Alumno para cada tarea 
habilidades = {
    'Alumno 1': {'Tarea A': 7, 'Tarea B': 5, 'Tarea C': 8},
    'Alumno 2': {'Tarea A': 8, 'Tarea B': 6, 'Tarea C': 7},
    'Alumno 3': {'Tarea A': 6, 'Tarea B': 8, 'Tarea C': 7},
}

# Restricciones: cada tarea debe ir a un alumno distinto
restricciones = { t: 'Unico' for t in tareas }

def contar_conflictos(asignacion, tarea, alumno):
    """Cuenta cuántas veces 'alumno' ya fue asignado a otra tarea."""
    return sum(1 for t, a in asignacion.items() if t != tarea and a == alumno)

def min_conflicts(tareas, alumnos, max_iter=1000):
    # Asignación inicial aleatoria
    asignacion = {tarea: random.choice(alumnos) for tarea in tareas}

    for _ in range(max_iter):
        # Buscar tareas en conflicto
        tareas_conflictivas = [t for t in tareas if contar_conflictos(asignacion, t, asignacion[t]) > 0]

        if not tareas_conflictivas:
            return asignacion  # No hay conflictos, solución válida

        tarea = random.choice(tareas_conflictivas)

        # Elegir el alumno que cause menos conflictos para esta tarea
        mejor_alumno = min(alumnos, key=lambda a: contar_conflictos(asignacion, tarea, a))
        asignacion[tarea] = mejor_alumno

    return None  # No se encontró solución dentro del límite
solucion = min_conflicts(tareas, alumnos)

if solucion:
    print("\nAsignación de tareas a alumnos (Mínimos-Conflictos):")
    for tarea, alumno in solucion.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
