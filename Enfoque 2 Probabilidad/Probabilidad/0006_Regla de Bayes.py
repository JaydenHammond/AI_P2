## Regla de Bayes calcula la probabilidad posterior de un evento dado evidencia usando la fórmula P(A|B) = P(B|A)·P(A) / P(B).
## f(A|B) = [P(B|A) × P(A)] / [∑ₐ P(B|Aₐ) × P(Aₐ)]; normaliza sobre todas las hipótesis Aₐ.

import random

# RECORDATORIO: Defino las hipótesis H1 y H2, por ejemplo, dos máquinas que pueden generar un defecto.
hipotesis = ['H1', 'H2']

# RECORDATORIO: P(H1) y P(H2) son mis creencias iniciales (priori).
P_prior = {
    'H1': 0.6,   # Creo que H1 es más probable antes de ver datos
    'H2': 0.4
}

# RECORDATORIO: P(evidencia|H) es la probabilidad de observar un defecto dado cada hipótesis.
P_likely = {
    'H1': 0.02,  # Si la máquina es H1, 2% de probabilidad de defecto
    'H2': 0.05   # Si es H2, 5% de probabilidad de defecto
}

# RECORDATORIO: Observamos un defecto, llamémoslo evento B.
evento = 'defecto'

# RECORDATORIO: Calculo numeradores para cada hipótesis: P(B|H)·P(H)
numeradores = {h: P_likely[h] * P_prior[h] for h in hipotesis}

# RECORDATORIO: Calculo P(B) sumando todos los numeradores (evidencia marginal).
P_evidencia = sum(numeradores.values())

# RECORDATORIO: Aplico Regla de Bayes y normalizo: P(H|B) = numerador / P(B)
P_posterior = {h: numeradores[h] / P_evidencia for h in hipotesis}

# RECORDATORIO: Ahora P_posterior contiene mis nuevas creencias tras ver el defecto.
print("\nProbabilidad posterior P(hipótesis | defecto):")
for h in hipotesis:
    print(f"P({h} | defecto) = {P_posterior[h]:.2f}")
