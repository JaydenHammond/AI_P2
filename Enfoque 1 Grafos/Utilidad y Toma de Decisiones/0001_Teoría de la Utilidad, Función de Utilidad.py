## Función de Utilidad es un modelo de decisión racional que asigna un valor numérico a cada alternativa según sus beneficios esperados, eligiendo la que maximiza la utilidad.
## f(n) = utilidad esperada; se elige la opción con mayor beneficio ponderado por las preferencias del decisor.

import random

# Opciones de becas disponibles
becas = ['Beca A', 'Beca B', 'Beca C']

# Criterios evaluados para cada beca (valores en escala de 0 a 10)
# Criterios: monto, prestigio, facilidad de obtenerla
caracteristicas = {
    'Beca A': {'monto': 9, 'prestigio': 6, 'facilidad': 4},
    'Beca B': {'monto': 6, 'prestigio': 9, 'facilidad': 5},
    'Beca C': {'monto': 7, 'prestigio': 7, 'facilidad': 8},
}

# Preferencias del alumno (pesos suman 1.0)
# El alumno valora más el prestigio que la facilidad o el monto
pesos_utilidad = {
    'monto': 0.3,
    'prestigio': 0.5,
    'facilidad': 0.2,
}

def calcular_utilidad(beca, caracteristicas, pesos):
    """Calcula la utilidad total para una beca dada."""
    return sum(caracteristicas[beca][crit] * pesos[crit] for crit in pesos)

def elegir_mejor_beca(becas, caracteristicas, pesos):
    """Elige la beca con mayor utilidad esperada."""
    utilidades = {beca: calcular_utilidad(beca, caracteristicas, pesos) for beca in becas}
    mejor_beca = max(utilidades, key=utilidades.get)
    return mejor_beca, utilidades[mejor_beca]
mejor_opcion, utilidad = elegir_mejor_beca(becas, caracteristicas, pesos_utilidad)

print("\nSelección óptima de beca basada en función de utilidad:")
print(f"Beca elegida: {mejor_opcion} (Utilidad: {utilidad:.2f})")
