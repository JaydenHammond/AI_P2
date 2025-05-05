## Red Bayesiana Dinámica (DBN) extiende una red bayesiana para modelar variables a lo largo del tiempo, capturando relaciones temporales y de transición.
## f(n) = P(Xₜ | Xₜ₋₁), donde se infiere el estado actual con base en creencias anteriores y las evidencias observadas en cada paso temporal.

# Estados ocultos y observaciones
estados = ['Soleado', 'Lluvioso']
observaciones = ['Ver sol', 'Ver paraguas']

# Distribución inicial
P_inicio = {
    'Soleado': 0.7,
    'Lluvioso': 0.3
}

# Transiciones
P_transicion = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.3, 'Lluvioso': 0.7}
}

# Modelo de observación P
P_observacion = {
    'Soleado': {'Ver sol': 0.9, 'Ver paraguas': 0.1},
    'Lluvioso': {'Ver sol': 0.2, 'Ver paraguas': 0.8}
}

def normalizar(distribucion):
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}

def filtrar(belief_anterior, observacion_actual):
    """Filtrado hacia adelante: actualiza la creencia usando transición y observación."""
    predicho = {}
    for estado_actual in estados:
        predicho[estado_actual] = sum(
            belief_anterior[estado_pasado] * P_transicion[estado_pasado][estado_actual]
            for estado_pasado in estados
        )
    
    actualizado = {
        estado: P_observacion[estado][observacion_actual] * predicho[estado]
        for estado in estados
    }
    
    return normalizar(actualizado)
secuencia_observaciones = ['Ver sol', 'Ver paraguas', 'Ver paraguas']

belief = P_inicio
for t, observacion in enumerate(secuencia_observaciones, 1):
    belief = filtrar(belief, observacion)
    print(f"\nPaso {t} | Observación: {observacion}")
    for estado, prob in belief.items():
        print(f"{estado}: {prob:.3f}")
