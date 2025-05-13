## Algoritmo Hacia Delante-Atrás (Forward-Backward) calcula las probabilidades forward (α) y backward (β) en un HMM para inferencia de estados ocultos.
## f(α, β) donde αₜ(s) = P(e₁:ₜ, Xₜ=s) y βₜ(s) = P(eₜ₊₁:ₙ | Xₜ=s), usados para estimar P(Xₜ | evidencia).

import random

# RECORDATORIO: defino los estados ocultos y las posibles observaciones.
estados = ['Lluvioso', 'Soleado']
observaciones = ['Lavar', 'Caminar', 'Limpiar']

# RECORDATORIO: modelo de transición P(Xₜ | Xₜ₋₁).
P_trans = {
    'Lluvioso': {'Lluvioso': 0.7, 'Soleado': 0.3},
    'Soleado':  {'Lluvioso': 0.4, 'Soleado': 0.6}
}

# RECORDATORIO: modelo de observación P(eₜ | Xₜ).
P_obs = {
    'Lluvioso': {'Lavar': 0.6, 'Caminar': 0.1, 'Limpiar': 0.3},
    'Soleado':  {'Lavar': 0.1, 'Caminar': 0.7, 'Limpiar': 0.2}
}

# RECORDATORIO: distribución inicial P(X₀).
P_inicio = {'Lluvioso': 0.5, 'Soleado': 0.5}

# RECORDATORIO: secuencia de evidencias observadas.
evidencias = ['Caminar', 'Limpiar', 'Lavar']

def forward_backward(evidencias):
    T = len(evidencias)
    # RECORDATORIO: inicializar α y β como listas de diccionarios por tiempo y estado.
    alpha = [ {s: 0.0 for s in estados} for _ in range(T) ]
    beta  = [ {s: 0.0 for s in estados} for _ in range(T) ]

    # -- Forward (α) --
    # RECORDATORIO: paso t=0
    for s in estados:
        alpha[0][s] = P_inicio[s] * P_obs[s][evidencias[0]]
    # RECORDATORIO: normalizar α₀
    total0 = sum(alpha[0].values())
    for s in estados:
        alpha[0][s] /= total0

    # RECORDATORIO: pasos t=1..T-1
    for t in range(1, T):
        for s in estados:
            suma = sum(alpha[t-1][sp] * P_trans[sp][s] for sp in estados)
            alpha[t][s] = suma * P_obs[s][evidencias[t]]
        # RECORDATORIO: normalizar αₜ
        total = sum(alpha[t].values())
        for s in estados:
            alpha[t][s] /= total

    # -- Backward (β) --
    # RECORDATORIO: βₙ = 1 para todos los estados
    for s in estados:
        beta[T-1][s] = 1.0

    # RECORDATORIO: pasos t=T-2..0
    for t in range(T-2, -1, -1):
        for s in estados:
            beta[t][s] = sum(
                P_trans[s][sp] * P_obs[sp][evidencias[t+1]] * beta[t+1][sp]
                for sp in estados
            )
        # RECORDATORIO: normalizar βₜ (opcional para estabilidad)
        total = sum(beta[t].values())
        for s in estados:
            beta[t][s] /= total

    return alpha, beta

# EJECUCIÓN
alpha, beta = forward_backward(evidencias)

# RESULTADO: mostrar αₜ(s) y βₜ(s)
print("\nForward (α):")
for t, a in enumerate(alpha):
    print(f" t={t}: {a}")

print("\nBackward (β):")
for t, b in enumerate(beta):
    print(f" t={t}: {b}")
