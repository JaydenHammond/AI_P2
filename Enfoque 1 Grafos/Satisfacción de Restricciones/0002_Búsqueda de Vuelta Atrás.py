## Búsqueda de Vuelta Atrás es una búsqueda informada que explora todas las posibilidades de manera recursiva, retrocediendo cuando encuentra que una asignación no es válida.
## f(n) = h(n), donde h es la evaluación de la satisfacción de las restricciones; si la asignación no es válida, se retrocede y prueba otra solución.

import random

# Tareas y alumnos
tareas = ['Tarea A', 'Tarea B', 'Tarea C']
alumnos = ['Alumno 1', 'Alumno 2', 'Alumno 3']

# Fortalezas de cada Alumno para cada tarea 
habilidades = {
    'Alumno 1': {'Tarea A': 7, 'Tarea B': 5, 'Tarea C': 8},
    'Alumno 2': {'Tarea A': 8, 'Tarea B': 6, 'Tarea C': 7},
    'Alumno 3': {'Tarea A': 6, 'Tarea B': 8, 'Tarea C': 7},

}

#No puede haber tareas duplicadas ni alumnos sin tareas asignadas.
restricciones = {
    'Tarea A': 'Unico',  
    'Tarea B': 'Unico',  
    'Tarea C': 'Unico',  
}

def es_valido(asignacion, restricciones):
    tareas_asignadas = set(asignacion.values())
    if len(tareas_asignadas) != len(asignacion):
        return False
    return True

def backtracking(asignacion, tareas, alumnos, habilidades, restricciones, index=0):
    if index == len(tareas):
        return asignacion

    tarea_actual = tareas[index]
    mejores_alumnos = sorted(alumnos, key=lambda alum: habilidades[alum].get(tarea_actual, 0), reverse=True)

    for alumno in mejores_alumnos:
        asignacion[tarea_actual] = alumno

        if es_valido(asignacion, restricciones):
            resultado = backtracking(asignacion, tareas, alumnos, habilidades, restricciones, index + 1)
            if resultado:
                return resultado

        asignacion.pop(tarea_actual)
    return None

asignacion_tareas = backtracking({}, tareas, alumnos, habilidades, restricciones)

# Resultado
if asignacion_tareas:
    print("\nAsignación de tareas a alumnos:")
    for tarea, alumno in asignacion_tareas.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
