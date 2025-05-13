## Filtrado, Predicción, Suavizado y Explicación aplican técnicas de HMM para mantener creencias sobre estados ocultos a lo largo del tiempo.
## f(α, β) donde αₜ = P(Xₜ | e₁:ₜ) (filtrado), predicción = P(Xₜ₊ₖ | e₁:ₜ), βₜ = P(eₜ₊₁:ₜ₊ₙ | Xₜ) (suavizado), explicación = argmax P(X₁:ₙ | e₁:ₙ).

import random

# RECORDATORIO: defino estados ocultos y observaciones posibles.
estados = ['Sunny', 'Rainy']
observaciones = ['Walk', 'Shop', 'Clean']

# RECORDATORIO: modelo de transición P(Xₜ | Xₜ₋₁).
P_trans = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},
    'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}
}

# RECORDATORIO: modelo de observación P(eₜ | Xₜ).
P_obs = {
    'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5}
}

# RECORDATORIO: distribución inicial P(X₀).
P_inicio = {'Sunny': 0.5, 'Rainy': 0.5}

# RECORDATORIO: secuencia de evidencias observadas.
evidencias = ['Walk', 'Shop', 'Clean']

# Función de filtrado (forward)
def filtrar(evidencias):
    alpha = []
    # t = 0: base
    a0 = {s: P_inicio[s] * P_obs[s][evidencias[0]] for s in estados}
    # RECORDATORIO: normalizar a0
    total0 = sum(a0.values())
    a0 = {s: a0[s] / total0 for s in estados}
    alpha.append(a0)
    # t > 0: recursión
    for t in range(1, len(evidencias)):
        a_prev = alpha[-1]
        a_t = {}
        for s in estados:
            # RECORDATORIO: suma sobre estados previos
            suma = sum(a_prev[sp] * P_trans[sp][s] for sp in estados)
            a_t[s] = suma * P_obs[s][evidencias[t]]
        # normalizar
        total = sum(a_t.values())
        a_t = {s: a_t[s] / total for s in estados}
        alpha.append(a_t)
    return alpha  # lista de αₜ

# Función de predicción k pasos adelante
def predecir(alpha_t, k):
    pred = alpha_t.copy()
    for _ in range(k):
        pred = {s: sum(pred[sp] * P_trans[sp][s] for sp in estados) for s in estados}
        # RECORDATORIO: no incluye evidencia nueva, solo transición
    # normalizar
    total = sum(pred.values())
    return {s: pred[s] / total for s in estados}

# Función de suavizado (forward-backward)
def suavizar(alpha, evidencias):
    # calcular β desde final hacia 0
    beta = [None] * len(evidencias)
    # βₙ = 1
    beta[-1] = {s: 1.0 for s in estados}
    for t in range(len(evidencias)-2, -1, -1):
        b_next = beta[t+1]
        b_t = {}
        for s in estados:
            # RECORDATORIO: suma sobre s' con transición y obs
            b_t[s] = sum(P_trans[s][sp] * P_obs[sp][evidencias[t+1]] * b_next[sp] for sp in estados)
        # no hace falta normalizar βₜ
        beta[t] = b_t
    # combinar α and β
    smooth = []
    for t in range(len(evidencias)):
        producto = {s: alpha[t][s] * beta[t][s] for s in estados}
        # normalizar
        total = sum(producto.values())
        smooth.append({s: producto[s] / total for s in estados})
    return smooth  # lista de P(Xₜ | e₁:ₙ)

# Función de explicación (Viterbi)
def explicar(evidencias):
    delta = []
    psi = []
    # inicialización
    d0 = {s: P_inicio[s] * P_obs[s][evidencias[0]] for s in estados}
    delta.append(d0)
    psi.append({s: None for s in estados})
    # recursión
    for t in range(1, len(evidencias)):
        d_t = {}
        psi_t = {}
        for s in estados:
            # RECORDATORIO: busco mejor antecesor
            candidatos = [(delta[t-1][sp] * P_trans[sp][s], sp) for sp in estados]
            max_val, argmax_sp = max(candidatos, key=lambda x: x[0])
            d_t[s] = max_val * P_obs[s][evidencias[t]]
            psi_t[s] = argmax_sp
        delta.append(d_t)
        psi.append(psi_t)
    # backtrack
    # RECORDATORIO: encuentro estado final más probable
    last_state = max(delta[-1], key=delta[-1].get)
    path = [last_state]
    for t in range(len(evidencias)-1, 0, -1):
        last_state = psi[t][last_state]
        path.insert(0, last_state)
    return path

# EJECUCIÓN
alpha = filtrar(evidencias)
print("\nFiltrado (α):")
for t, a in enumerate(alpha):
    print(f" t={t}: {a}")

pred_1 = predecir(alpha[-1], 1)
print(f"\nPredicción 1 paso adelante tras t={len(evidencias)-1}: {pred_1}")

smooth = suavizar(alpha, evidencias)
print("\nSuavizado P(Xₜ | evidencias completas):")
for t, s in enumerate(smooth):
    print(f" t={t}: {s}")

mejor_camino = explicar(evidencias)
print(f"\nExplicación (Viterbi path): {mejor_camino}")
