## Ponderación de Verosimilitud usa muestreo dirigido por evidencia, asignando pesos a las muestras según la probabilidad de la evidencia observada.
## f(Q | e) ≈ ∑_{i=1}^N w_i · 1[Q_i = q] / ∑_{i=1}^N w_i; donde w_i es el peso de la muestra i.

# RECORDATORIO: import random para generar números aleatorios uniformes.
import random

# RECORDATORIO: defino variables y dominios para la red (Rain, Sprinkler, WetGrass).
variables = ['Rain', 'Sprinkler', 'WetGrass']
valores = ['True', 'False']

# RECORDATORIO: probabilidades a priori y CPTs.
P_Rain = {'True': 0.2, 'False': 0.8}
P_Sprinkler = {
    'True':  {'True': 0.01, 'False': 0.99},
    'False': {'True': 0.4,  'False': 0.6}
}
P_WetGrass = {
    ('True',  'True'):  0.99,
    ('True',  'False'): 0.9,
    ('False', 'True'):  0.9,
    ('False', 'False'): 0.0
}

# RECORDATORIO: evidencia observada
evidence = {'WetGrass': 'True'}

def sample_and_weight(evidence):
    """Genera una muestra consistente con la red, asigna peso según evidencia."""
    weight = 1.0
    sample = {}
    # RECORDATORIO: muestreo de Rain (sin padres)
    r = random.random()
    for v in valores:
        if r < P_Rain[v]:
            sample['Rain'] = v
            break
        r -= P_Rain[v]
    # RECORDATORIO: no influye en peso porque Rain no está en evidencia

    # RECORDATORIO: muestreo de Sprinkler dado Rain
    r = random.random()
    for v in valores:
        p = P_Sprinkler[sample['Rain']][v]
        if r < p:
            sample['Sprinkler'] = v
            break
        r -= p
    # RECORDATORIO: Sprinkler no está en evidencia → peso no cambia

    # RECORDATORIO: muestreo pesado de WetGrass dado Rain y Sprinkler
    # Si WetGrass está en evidencia, ajusto peso en lugar de muestrear libremente
    if 'WetGrass' in evidence:
        # RECORDATORIO: peso = P(evidence | parents)
        key = (sample['Rain'], sample['Sprinkler'])
        pw = P_WetGrass[key] if evidence['WetGrass'] == 'True' else 1 - P_WetGrass[key]
        weight *= pw
        # RECORDATORIO: fijo el valor de WetGrass en la muestra
        sample['WetGrass'] = evidence['WetGrass']
    else:
        r = random.random()
        key = (sample['Rain'], sample['Sprinkler'])
        p = P_WetGrass[key]
        sample['WetGrass'] = 'True' if r < p else 'False'

    return sample, weight

def likelihood_weighting(query_var, evidence, N=10000):
    """Estima P(query_var = True | evidence) usando ponderación de verosimilitud."""
    counts = {v: 0.0 for v in valores}
    total_weight = 0.0

    for _ in range(N):
        sample, w = sample_and_weight(evidence)
        counts[sample[query_var]] += w
        total_weight += w

    # RECORDATORIO: normalizo para obtener la distribución posterior
    return {v: counts[v] / total_weight for v in valores}

# RECORDATORIO: estimar P(Rain | WetGrass = True)
posterior = likelihood_weighting('Rain', evidence, N=5000)

# RESULTADO
print("\nPonderación de Verosimilitud P(Rain | WetGrass=True):")
for v in valores:
    print(f"P(Rain={v} | WetGrass=True) ≈ {posterior[v]:.3f}")
