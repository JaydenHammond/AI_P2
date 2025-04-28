## Comprobación Hacia Delante es una búsqueda informada que utiliza reducción de dominios para detectar conflictos tempranamente tras cada asignación.
## f(n) = h(n), donde h es la evaluación de la satisfacción de las restricciones; se podan los valores inconsistentes antes de profundizar en la búsqueda.

import random
import copy

# Tareas y alumnos
tareas = ['Tarea A', 'Tarea B', 'Tarea C']
alumnos = ['Alumno 1', 'Alumno 2', 'Alumno 3']

# Fortalezas de cada Alumno para cada tarea 
habilidades = {
    'Alumno 1': {'Tarea A': 7, 'Tarea B': 5, 'Tarea C': 8},
    'Alumno 2': {'Tarea A': 8, 'Tarea B': 6, 'Tarea C': 7},
    'Alumno 3': {'Tarea A': 6, 'Tarea B': 8, 'Tarea C': 7},
}

# No puede haber tareas duplicadas ni alumnos sin tareas asignadas.
restricciones = {
    'Tarea A': 'Unico',  
    'Tarea B': 'Unico',  
    'Tarea C': 'Unico',  
}

def es_valido(asignacion, restricciones):
    tareas_asignadas = set(asignacion.values())
    return len(tareas_asignadas) == len(asignacion)

def forward_checking(asignacion, tareas, dominios, restricciones):
    if len(asignacion) == len(tareas):
        return asignacion

    idx = len(asignacion)
    tarea_actual = tareas[idx]

    for alumno in dominios[tarea_actual]:
        asignacion[tarea_actual] = alumno

        if not es_valido(asignacion, restricciones):
            asignacion.pop(tarea_actual)
            continue

        nuevos_dominios = copy.deepcopy(dominios)
        consistent = True
        for tarea in tareas:
            if tarea not in asignacion and restricciones[tarea] == 'Unico':
                if alumno in nuevos_dominios[tarea]:
                    nuevos_dominios[tarea].remove(alumno)
                if not nuevos_dominios[tarea]:
                    consistent = False
                    break

        if not consistent:
            asignacion.pop(tarea_actual)
            continue
        resultado = forward_checking(asignacion, tareas, nuevos_dominios, restricciones)
        if resultado:
            return resultado
        asignacion.pop(tarea_actual)

    return None

dominios_iniciales = {t: alumnos.copy() for t in tareas}

asignacion_tareas = forward_checking({}, tareas, dominios_iniciales, restricciones)

# Resultado
if asignacion_tareas:
    print("\nAsignación de tareas a alumnos (Forward Checking):")
    for tarea, alumno in asignacion_tareas.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
