## Eliminación de Variables calcula distribuciones posteriores eliminando factor a factor las variables no query.
## f(Q | e) = α ∏_{f ∈ F} ∑_{h} f(...), donde h son variables ocultas; elimina h mediante sum-product en factores.

import itertools

# RECORDATORIO: variables y su dominio.
variables = ['Rain', 'Sprinkler', 'WetGrass']
valores = ['True', 'False']

# RECORDATORIO: Defino los factores (CPTs) como diccionarios: factor(variable(s)) = probabilidad.
# Factor para Rain: P(Rain)
factor_Rain = {('Rain', r): p for r, p in zip(valores, [0.2, 0.8])}

# RECORDATORIO: Factor para Sprinkler dado Rain: P(Sprinkler | Rain)
factor_Sprinkler = {}
for r in valores:
    probs = [0.01, 0.99] if r == 'True' else [0.4, 0.6]
    for s, p in zip(valores, probs):
        factor_Sprinkler[('Rain', r, 'Sprinkler', s)] = p

# RECORDATORIO: Factor para WetGrass dado Rain y Sprinkler: P(WetGrass | Rain, Sprinkler)
factor_Wet = {}
cpt = {
    ('True','True'):  0.99,
    ('True','False'): 0.9,
    ('False','True'): 0.9,
    ('False','False'): 0.0
}
for r, s in cpt:
    for w in valores:
        p = cpt[(r, s)] if w == 'True' else 1 - cpt[(r, s)]
        factor_Wet[('Rain', r, 'Sprinkler', s, 'WetGrass', w)] = p

# RECORDATORIO: Evidence: WetGrass = True
evidence = {'WetGrass': 'True'}

# RECORDATORIO: Función para multiplicar factores y sumar sobre una variable.
def multiply(f1, f2):
    result = {}
    # RECORDATORIO: combinamos claves de f1 y f2 conservando coincidencias
    for k1, p1 in f1.items():
        for k2, p2 in f2.items():
            # extraer asignaciones como diccionario
            asig = {}
            for i in range(0, len(k1), 2): asig[k1[i]] = k1[i+1]
            for i in range(0, len(k2), 2): asig[k2[i]] = k2[i+1]
            # si hay conflicto en asignaciones, ignorar
            if any(asig[var] != val for var, val in asig.items() if (var, val) not in zip(k1+k2, k1[1::2]+k2[1::2])): 
                continue
            # generar clave ordenada
            claves = tuple(sum(([var, asig[var]] for var in sorted(asig)), []))
            result[claves] = result.get(claves, 0) + p1 * p2
    return result

def sum_out(factor, var):
    result = {}
    # RECORDATORIO: para cada entrada del factor, sumo p sobre var
    for k, p in factor.items():
        asig = {k[i]: k[i+1] for i in range(0, len(k), 2)}
        asig.pop(var, None)  # elimino var
        claves = tuple(sum(([v, asig[v]] for v in sorted(asig)), []))
        result[claves] = result.get(claves, 0) + p
    return result

# RECORDATORIO: Paso 1: restringir factores con evidencia WetGrass=True
def restrict(factor, var, val):
    result = {}
    for k, p in factor.items():
        asig = {k[i]: k[i+1] for i in range(0, len(k), 2)}
        if var in asig and asig[var] != val:
            continue
        # mantenemos la asignación completa
        result[k] = p
    return result

fR = factor_Rain
fS = factor_Sprinkler
fW = restrict(factor_Wet, 'WetGrass', 'True')

# RECORDATORIO: Paso 2: elimino Sprinkler → sum_out en fS y fW combinados con fR
# Primero multiplico fS y fW
fSW = multiply(fS, fW)
# Luego sumo Sprinkler
fSW_sum = sum_out(fSW, 'Sprinkler')

# RECORDATORIO: Paso 3: multiplico con fR y sumo si hubiera más ocultas
f_all = multiply(fR, fSW_sum)
# Aquí solo queda Rain, combinamos
# ya no hay variables ocultas, f_all es factor sobre Rain

# RECORDATORIO: Normalizo para obtener P(Rain | WetGrass=True)
total = sum(f_all.values())
P_posterior = {k[1]: p/total for k, p in f_all.items()}

# RESULTADO
print("\nP(Rain | WetGrass=True) por Eliminación de Variables:")
for r, prob in P_posterior.items():
    print(f"P(Rain={r} | WetGrass=True) = {prob:.2f}")
