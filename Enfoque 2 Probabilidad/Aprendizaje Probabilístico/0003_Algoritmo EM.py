## Algoritmo EM estima parámetros de un modelo de mezcla cuando faltan etiquetas (datos incompletos).
## f(θ) = log P(data | θ), iteramos E-step (estimación de responsabilidades) y M-step (reestimación de θ).

import random
import math

# RECORDATORIO: datos observados: secuencias de lanzamientos con número de caras en 10 tiradas.
# Cada experimento proviene de una de dos monedas A y B, pero no sabemos cuál.
datos = [7, 6, 9, 8, 2, 3, 4, 5, 1, 0]  # cada número es caras en 10 lanzamientos
n = 10  # número de tiradas por experimento

# RECORDATORIO: inicializamos parámetros al azar
pi = 0.5             # peso de la moneda A en la mezcla
pA = 0.6             # sesgo inicial de la moneda A
pB = 0.4             # sesgo inicial de la moneda B

# EM iterations
for iter in range(10):
    # E-STEP: calcular responsabilidades γ_i para cada dato
    gammas = []
    for k in datos:
        # RECORDATORIO: probabilidad de k caras bajo cada moneda (binomial)
        PA = pi * (math.comb(n, k) * pA**k * (1-pA)**(n-k))
        PB = (1-pi) * (math.comb(n, k) * pB**k * (1-pB)**(n-k))
        total = PA + PB or 1e-12
        gamma = PA / total
        gammas.append(gamma)
    # M-STEP: reestimar π, pA, pB usando γ
    # RECORDATORIO: π = promedio de γ
    pi = sum(gammas) / len(datos)
    # RECORDATORIO: pA = ∑ γ_i * k_i / (∑ γ_i * n)
    pA = sum(g * k for g, k in zip(gammas, datos)) / (sum(gammas) * n)
    # RECORDATORIO: pB = ∑ (1-γ_i) * k_i / (∑ (1-γ_i) * n)
    pB = sum((1-g) * k for g, k in zip(gammas, datos)) / (sum(1-g for g in gammas) * n)

# RESULTADO: mostrar parámetros estimados
print("Parámetros estimados tras EM:")
print(f"Mezcla π (moneda A): {pi:.3f}")
print(f"Sesgo pA (moneda A): {pA:.3f}")
print(f"Sesgo pB (moneda B): {pB:.3f}")
