## Inferencia por Enumeración permite calcular distribuciones posteriores sumando sobre las variables ocultas.
## f(Q | e) = α ∑_{h} ∏_{X_i} P(X_i | Parents(X_i)), donde h son las variables no observadas.

import itertools

# RECORDATORIO: defino las variables de la red y sus posibles valores.
variables = ['Rain', 'Sprinkler', 'WetGrass']
valores = ['True', 'False']

# RECORDATORIO: CPT de Rain (sin padres): P(Rain)
P_Rain = {'True': 0.2, 'False': 0.8}

# RECORDATORIO: CPT de Sprinkler dado Rain: P(Sprinkler | Rain)
P_Sprinkler = {
    'True':  {'True': 0.01, 'False': 0.99},
    'False': {'True': 0.4,  'False': 0.6}
}

# RECORDATORIO: CPT de WetGrass dado Rain y Sprinkler: P(WetGrass | Rain, Sprinkler)
P_WetGrass = {
    ('True',  'True'):  0.99,
    ('True',  'False'): 0.9,
    ('False', 'True'):  0.9,
    ('False', 'False'): 0.0
}

# RECORDATORIO: Queremos P(Rain | WetGrass = True). Evidence: WetGrass=True.
evidence = {'WetGrass': 'True'}

# RECORDATORIO: función para calcular la probabilidad conjunta de una asignación completa.
def prob_joint(asig):
    p = P_Rain[asig['Rain']]
    p *= P_Sprinkler[asig['Rain']][asig['Sprinkler']]
    key = (asig['Rain'], asig['Sprinkler'])
    p *= P_WetGrass[(asig['Rain'], asig['Sprinkler'])] if asig['WetGrass'] == 'True' else (1 - P_WetGrass[key])
    return p

# RECORDATORIO: sumo sobre la variable oculta Sprinkler
# para cada valor de Rain ('True', 'False') calculo:
# numerador = ∑_{sprinkler} P(Rain, Sprinkler, WetGrass=True)
numeradores = {}
for r in valores:
    total = 0.0
    for s in valores:
        asig = {'Rain': r, 'Sprinkler': s, 'WetGrass': 'True'}
        total += prob_joint(asig)
    numeradores[r] = total

# RECORDATORIO: normalizo para que P(True|e) + P(False|e) = 1
normalizador = sum(numeradores.values())
P_posterior = {r: numeradores[r] / normalizador for r in valores}

# RESULTADO: muestro la distribución posterior de Rain dado WetGrass=True
print("\nInferencia por Enumeración P(Rain | WetGrass=True):")
for r in valores:
    print(f"P(Rain={r} | WetGrass=True) = {P_posterior[r]:.2f}")
