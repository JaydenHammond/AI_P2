## Modelos de Markov Ocultos usan estados ocultos y observaciones para estimar creencias mediante el algoritmo forward.
## f(α) donde αₜ(s) = P(Xₜ=s | e₁:ₜ) ∝ P(eₜ | s) · ∑ₛₚ αₜ₋₁(sₚ)·P(s | sₚ)

# RECORDATORIO: definimos dos estados ocultos, por ejemplo: 'Frío' y 'Calor'.
estados = ['Frío', 'Calor']

# RECORDATORIO: posibles observaciones, por ejemplo: 'Caminar', 'Leer'.
observaciones = ['Caminar', 'Leer', 'Correr']

# RECORDATORIO: distribución inicial π = P(X₀)
pi = {'Frío': 0.6, 'Calor': 0.4}

# RECORDATORIO: matriz de transición A = P(Xₜ | Xₜ₋₁)
A = {
    'Frío': {'Frío': 0.7, 'Calor': 0.3},
    'Calor': {'Frío': 0.4, 'Calor': 0.6},
}

# RECORDATORIO: matriz de emisión B = P(e | Xₜ)
B = {
    'Frío':  {'Caminar': 0.2, 'Leer': 0.5, 'Correr': 0.3},
    'Calor': {'Caminar': 0.6, 'Leer': 0.1, 'Correr': 0.3},
}

# RECORDATORIO: secuencia observada
secuencia = ['Caminar', 'Leer', 'Correr', 'Caminar']

def forward(secuencia):
    """Aplica filtrado forward y retorna lista de α normalizados por paso."""
    alpha = []
    # t = 0: α₀(s) ∝ π(s)·B(s, e₀)
    a0 = {s: pi[s] * B[s][secuencia[0]] for s in estados}
    total0 = sum(a0.values())
    a0 = {s: a0[s]/total0 for s in estados}
    alpha.append(a0)
    # t > 0: αₜ(s) ∝ B(s, eₜ) · ∑ₛₚ αₜ₋₁(sₚ)·A(s | sₚ)
    for t in range(1, len(secuencia)):
        et = secuencia[t]
        at = {}
        for s in estados:
            suma = sum(alpha[t-1][sp] * A[sp][s] for sp in estados)  # RECORDATORIO: sumar sobre previos
            at[s] = B[s][et] * suma                                # RECORDATORIO: peso por emisión
        total = sum(at.values())
        at = {s: at[s]/total for s in estados}                   # RECORDATORIO: normalizar αₜ
        alpha.append(at)
    return alpha

alpha = forward(secuencia)

# RESULTADO: mostramos creencias en cada paso
print("Filtrado Forward (α) paso a paso:")
for t, a in enumerate(alpha):
    print(f" t={t}: {a}")
