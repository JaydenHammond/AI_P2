## Redes de Decisión combinan probabilidad, utilidad y decisiones en una estructura dirigida para seleccionar la acción con mayor valor esperado.
## f(n) = ∑[P(estado) × U(acción, estado)]; se elige la acción que maximiza la utilidad esperada bajo incertidumbre.

import random

# Acciones posibles de un robot en una fábrica
acciones = ['Inspeccionar', 'Reparar', 'Ignorar']

# Estados posibles del sistema
estados = ['Falla Grave', 'Falla Leve', 'Sin Falla']

# Probabilidades de cada estado (incertidumbre)
probabilidades = {
    'Falla Grave': 0.2,
    'Falla Leve': 0.3,
    'Sin Falla':  0.5,
}

# Utilidad de cada acción en cada estado
utilidad = {
    'Inspeccionar': {'Falla Grave': 8, 'Falla Leve': 6, 'Sin Falla': 2},
    'Reparar':      {'Falla Grave': 10, 'Falla Leve': 4, 'Sin Falla': -3},
    'Ignorar':      {'Falla Grave': -10, 'Falla Leve': -2, 'Sin Falla': 5},
}

def calcular_utilidad_esperada(accion, probabilidades, utilidad):
    """Suma ponderada de la utilidad de una acción bajo todos los estados posibles."""
    return sum(probabilidades[estado] * utilidad[accion][estado] for estado in estados)

def mejor_decision(acciones, probabilidades, utilidad):
    """Selecciona la acción con mayor utilidad esperada."""
    utilidades_esperadas = {accion: calcular_utilidad_esperada(accion, probabilidades, utilidad) for accion in acciones}
    mejor = max(utilidades_esperadas, key=utilidades_esperadas.get)
    return mejor, utilidades_esperadas[mejor]
accion_optima, valor_esperado = mejor_decision(acciones, probabilidades, utilidad)

print("\nDecisión óptima basada en Red de Decisión:")
print(f"Acción recomendada: {accion_optima} (Utilidad esperada: {valor_esperado:.2f})")
