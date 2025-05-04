## Salto Atrás Dirigido por Conflictos es una búsqueda informada que retrocede directamente a la variable responsable del conflicto, evitando explorar caminos inválidos.
## f(n) = h(n), donde h evalúa la consistencia de la asignación; si ocurre un conflicto, se retrocede a la tarea que lo causó, no solo a la anterior.

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

# Restricciones: cada tarea debe ser asignada a un alumno diferente
restricciones = { t: 'Unico' for t in tareas }

def conflicto(asignacion, tarea, alumno):
    """Revisa si asignar 'alumno' a 'tarea' causa conflicto con otra tarea ya asignada."""
    for t_existente, a_existente in asignacion.items():
        if a_existente == alumno:
            return True, t_existente  # Conflicto con la tarea t_existente
    return False, None

def salto_atras_dirigido_conflictos(tareas, alumnos):
    return backjump({}, 0, {}, tareas, alumnos)

def backjump(asignacion, idx, causas_conflicto, tareas, alumnos):
    if idx == len(tareas):
        return asignacion  # Asignación completa sin conflictos

    tarea_actual = tareas[idx]
    causas_conflicto[tarea_actual] = set()
    for alumno in alumnos:
        hay_conflicto, tarea_conflictiva = conflicto(asignacion, tarea_actual, alumno)
        if not hay_conflicto:
            asignacion[tarea_actual] = alumno
            resultado = backjump(asignacion, idx + 1, causas_conflicto, tareas, alumnos)
            if resultado:
                return resultado
            # Si falló más adelante, agregamos causas acumuladas al conflicto actual
            causas_conflicto[tarea_actual].update(causas_conflicto.get(tareas[idx + 1], set()))
        else:
            causas_conflicto[tarea_actual].add(tarea_conflictiva)

    # No se pudo asignar esta tarea → saltar atrás al conflicto más reciente
    if causas_conflicto[tarea_actual]:
        conflicto_mas_reciente = max(tareas.index(c) for c in causas_conflicto[tarea_actual])
        nueva_asignacion = {t: a for t, a in asignacion.items() if tareas.index(t) <= conflicto_mas_reciente}
        return backjump(nueva_asignacion, conflicto_mas_reciente, causas_conflicto, tareas, alumnos)

    return None  # Fallo total

solucion = salto_atras_dirigido_conflictos(tareas, alumnos)

if solucion:
    print("\nAsignación de tareas a alumnos (Salto Atrás Dirigido por Conflictos):")
    for tarea, alumno in solucion.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
