## Propagación de Restricciones es una búsqueda informada que mantiene consistencia de arcos para podar dominios antes de profundizar en la búsqueda.
## f(n) = h(n), donde h es la evaluación de la satisfacción de las restricciones; se asegura la eliminación temprana de valores inconsistentes vía ac-3.

import random
import copy
from collections import deque

# Tareas y alumnos
tareas  = ['Tarea A', 'Tarea B', 'Tarea C']
alumnos = ['Alumno 1', 'Alumno 2', 'Alumno 3']

# Fortalezas de cada Alumno para cada tarea 
habilidades = {
    'Alumno 1': {'Tarea A': 7, 'Tarea B': 5, 'Tarea C': 8},
    'Alumno 2': {'Tarea A': 8, 'Tarea B': 6, 'Tarea C': 7},
    'Alumno 3': {'Tarea A': 6, 'Tarea B': 8, 'Tarea C': 7},
}

# Restricciones: cada tarea debe ir a un único alumno
restricciones = { t: 'Unico' for t in tareas }

def revise(dominios, Xi, Xj):
    """Revisa el dominio de Xi respecto a Xj para la restricción 'Unico'."""
    revisado = False
    for x in dominios[Xi][:]:
        if not any(x != y for y in dominios[Xj]):
            dominios[Xi].remove(x)
            revisado = True
    return revisado

def ac3(dominios):
    """Aplica AC-3 para hacer consistentes todos los arcos entre variables."""
    # Cola de todos los pares ordenados (Xi, Xj), Xi != Xj
    cola = deque((Xi, Xj) for Xi in tareas for Xj in tareas if Xi != Xj)
    while cola:
        Xi, Xj = cola.popleft()
        if revise(dominios, Xi, Xj):
            if not dominios[Xi]:
                return False  # Dominio vacío -> falla
            for Xk in tareas:
                if Xk not in (Xi, Xj):
                    cola.append((Xk, Xi))
    return True

def propagacion_restricciones(asignacion, dominios):
    if not ac3(dominios):
        return None
    if len(asignacion) == len(tareas):
        return asignacion

    idx = len(asignacion)
    tarea_actual = tareas[idx]
    for alumno in dominios[tarea_actual]:
        nueva_asign = asignacion.copy()
        nueva_asign[tarea_actual] = alumno
        nuevos_dom = copy.deepcopy(dominios)
        nuevos_dom[tarea_actual] = [alumno]
        resultado = propagacion_restricciones(nueva_asign, nuevos_dom)
        if resultado:
            return resultado

    return None

# Cualquier alumno para cualquier tarea
dominios_iniciales = { t: alumnos.copy() for t in tareas }
solucion = propagacion_restricciones({}, dominios_iniciales)

# Resultado
if solucion:
    print("\nAsignación de tareas a alumnos (Propagación de Restricciones):")
    for tarea, alumno in solucion.items():
        print(f"{tarea}: {alumno}")
else:
    print("No se pudo encontrar una asignación válida de tareas.")
