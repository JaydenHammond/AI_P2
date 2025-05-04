## Acondicionamiento del Corte es una técnica de reducción de problemas que elimina una o más variables (el corte), resuelve el resto, y luego reintegra las eliminadas consistentemente.
## f(n) = h(n), donde h es la cantidad de conflictos al reintegrar el corte al problema ya resuelto.

import random
import itertools

# Tareas y alumnos
tareas  = ['Tarea A', 'Tarea B', 'Tarea C']
alumnos = ['Alumno 1', 'Alumno 2', 'Alumno 3']

# Fortalezas de cada Alumno para cada tarea 
habilidades = {
    'Alumno 1': {'Tarea A': 7, 'Tarea B': 5, 'Tarea C': 8},
    'Alumno 2': {'Tarea A': 8, 'Tarea B': 6, 'Tarea C': 7},
    'Alumno 3': {'Tarea A': 6, 'Tarea B': 8, 'Tarea C': 7},
}

# Restricciones: cada tarea debe ir a un alumno diferente
restricciones = { t: 'Unico' for t in tareas }

def es_valido(asignacion):
    """Verifica que no haya alumnos repetidos."""
    return len(set(asignacion.values())) == len(asignacion)

def resolver_subproblema(tareas_sub, alumnos_disponibles):
    """Resuelve el subproblema con asignación por fuerza bruta válida."""
    for perm in itertools.permutations(alumnos_disponibles, len(tareas_sub)):
        asignacion = dict(zip(tareas_sub, perm))
        if es_valido(asignacion):
            return asignacion
    return None

def acondicionamiento_del_corte(tareas, alumnos, corte):
    tareas_subproblema = [t for t in tareas if t not in corte]
    alumnos_disponibles = alumnos.copy()

    # Resolver subproblema sin las tareas del corte
    asignacion_base = resolver_subproblema(tareas_subproblema, alumnos_disponibles)
    if not asignacion_base:
        return None

    # Quitar alumnos ya asignados del subproblema
    alumnos_restantes = [a for a in alumnos if a not in asignacion_base.values()]

    # Intentar reintegrar el corte sin conflictos
    asignacion_corte = resolver_subproblema(corte, alumnos_restantes)
    if not asignacion_corte:
        return None

    # Unir ambas asignaciones
    asignacion_base.update(asignacion_corte)
    return asignacion_base

corte = ['Tarea C']
solucion = acondicionamiento_del_corte(tareas, alumnos, corte)
if solucion:
    print("\nAsignación de tareas a alumnos (Acondicionamiento del Corte):")
    for tarea, alumno in solucion.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
