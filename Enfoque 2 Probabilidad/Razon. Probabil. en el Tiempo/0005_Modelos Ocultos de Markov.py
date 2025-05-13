## Modelo Oculto de Markov (HMM) modela procesos con estados ocultos y observaciones visibles, conectados por probabilidades de transición y emisión.
## f(n) = (S, O, A, B, π) donde S = estados ocultos, O = observaciones, A = matriz de transición, B = matriz de emisión, π = distribución inicial.

import random

# RECORDATORIO: no necesitamos librerías externas más allá de random para este ejemplo.
# Estados ocultos del HMM
estados = ['Lluvioso', 'Soleado']

# Observaciones posibles
observaciones = ['Caminar', 'Comprar', 'Limpiar']

# RECORDATORIO: π = P(X₀) distribución inicial sobre estados
pi = {'Lluvioso': 0.6, 'Soleado': 0.4}

# RECORDATORIO: A = P(Xₜ | Xₜ₋₁) matriz de transición
A = {
    'Lluvioso': {'Lluvioso': 0.7, 'Soleado': 0.3},
    'Soleado':  {'Lluvioso': 0.4, 'Soleado': 0.6}
}

# RECORDATORIO: B = P(Oₜ | Xₜ) matriz de emisión
B = {
    'Lluvioso': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5},
    'Soleado':  {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1}
}

# Simulación de una secuencia de longitud T
def simular_hmm(T):
    sec_estados = []
    sec_obs = []
    # RECORDATORIO: muestreo inicial según π
    r = random.random()
    acumulado = 0.0
    for s, p in pi.items():
        acumulado += p
        if r < acumulado:
            estado = s
            break
    sec_estados.append(estado)
    # RECORDATORIO: muestreo de emisión para t=0
    r = random.random()
    acumulado = 0.0
    for o, p in B[estado].items():
        acumulado += p
        if r < acumulado:
            sec_obs.append(o)
            break
    # pasos 1..T-1
    for _ in range(1, T):
        # RECORDATORIO: transición de estado
        r = random.random()
        acumulado = 0.0
        for s2, p in A[estado].items():
            acumulado += p
            if r < acumulado:
                estado = s2
                break
        sec_estados.append(estado)
        # RECORDATORIO: emisión dada nuevo estado
        r = random.random()
        acumulado = 0.0
        for o, p in B[estado].items():
            acumulado += p
            if r < acumulado:
                sec_obs.append(o)
                break
    return sec_estados, sec_obs

# Viterbi: decodificación del camino más probable dado la secuencia de observaciones
def viterbi(obs_seq):
    T = len(obs_seq)
    # δ y ψ
    delta = [{s: pi[s] * B[s][obs_seq[0]] for s in estados}]
    psi   = [{s: None for s in estados}]
    # RECORDATORIO: inicialización en t=0
    for t in range(1, T):
        delta.append({})
        psi.append({})
        for s in estados:
            # RECORDATORIO: para cada estado calculo max sobre prev δ·A
            candidatos = [(delta[t-1][sp] * A[sp][s], sp) for sp in estados]
            max_val, argmax_sp = max(candidatos, key=lambda x: x[0])
            delta[t][s] = max_val * B[s][obs_seq[t]]
            psi[t][s] = argmax_sp
    # RECORDATORIO: reconstrucción del camino óptimo
    path = [None] * T
    # estado final más probable
    last_state = max(delta[T-1], key=delta[T-1].get)
    path[T-1] = last_state
    for t in range(T-1, 0, -1):
        path[t-1] = psi[t][path[t]]
    return path

# EJECUCIÓN
T = 10  # longitud de la secuencia
hidden_seq, obs_seq = simular_hmm(T)
decoded_seq = viterbi(obs_seq)

# RESULTADO
print("\nSecuencia oculta simulada:   ", hidden_seq)
print("Secuencia observada:         ", obs_seq)
print("Camino Viterbi decodificado: ", decoded_seq)
