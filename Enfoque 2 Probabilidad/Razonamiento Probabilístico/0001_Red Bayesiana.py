## Red Bayesiana permite representar dependencias probabilísticas entre variables usando un grafo dirigido acíclico.
## f(n) = ∏ P(n | padres(n)), donde cada nodo multiplica su CPT condicional sobre sus padres.

import itertools

# RECORDATORIO: Defino las variables de la red: Lluvia (Rain), Aspersor (Sprinkler) y Césped Mojado (WetGrass).
variables = ['Rain', 'Sprinkler', 'WetGrass']

# RECORDATORIO: CPT de Rain (no tiene padres): P(Rain).
P_Rain = {'True': 0.2, 'False': 0.8}

# RECORDATORIO: CPT de Sprinkler dado Rain: P(Sprinkler | Rain).
P_Sprinkler = {
    'True':  {'True': 0.01, 'False': 0.99},  # si llueve, aspersor raramente está encendido
    'False': {'True': 0.4,  'False': 0.6}    # si no llueve, aspersor se enciende con prob 0.4
}

# RECORDATORIO: CPT de WetGrass dado Sprinkler y Rain: P(WetGrass | Sprinkler, Rain).
P_WetGrass = {
    ('True',  'True'):  0.99,  # si llueve y aspersor ON, césped casi seguro mojado
    ('True',  'False'): 0.9,   # si llueve y aspersor OFF, césped mojado por lluvia
    ('False', 'True'):  0.9,   # si no llueve y aspersor ON, césped mojado por aspersor
    ('False', 'False'): 0.0    # si no llueve y aspersor OFF, césped seco
}

# RECORDATORIO: Queremos calcular P(Rain | WetGrass = True) usando inferencia por enumeración.
# Paso 1: calcular la probabilidad conjunta para cada asignación completa.
def probabilidad_conjunta(asig):
    # P(Rain) × P(Sprinkler | Rain) × P(WetGrass | Sprinkler, Rain)
    p = P_Rain[asig['Rain']]
    p *= P_Sprinkler[asig['Rain']][asig['Sprinkler']]
    key = (asig['Sprinkler'], asig['Rain'])
    p *= P_WetGrass[key]
    return p

# RECORDATORIO: Genero todas las asignaciones posibles de True/False.
asignaciones = [dict(zip(variables, vals))
                for vals in itertools.product(['True','False'], repeat=3)]

# Paso 2: sumar numeradores para Rain=True y Rain=False condicionados a WetGrass=True.
numeradores = {'True': 0.0, 'False': 0.0}
for asig in asignaciones:
    if asig['WetGrass'] == 'True':
        numeradores[asig['Rain']] += probabilidad_conjunta(asig)

# RECORDATORIO: Normalizo para obtener la posterior P(Rain | WetGrass=True).
evidencia = sum(numeradores.values())
P_posterior = {r: numeradores[r]/evidencia for r in numeradores}

# RESULTADO
print("\nP(Rain | WetGrass = True):")
for r, prob in P_posterior.items():
    print(f"P(Rain={r} | WetGrass=True) = {prob:.2f}")
