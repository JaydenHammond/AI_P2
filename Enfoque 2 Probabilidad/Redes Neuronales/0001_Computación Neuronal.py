## Computación Neuronal simula una neurona artificial que recibe múltiples entradas, las pondera, y aplica una función de activación para generar una salida.
## f(x) = activación(peso·entrada + sesgo); se usa para clasificar patrones simples como compuertas lógicas.

import math  # RECORDATORIO: usamos math para la función sigmoide

# RECORDATORIO: función sigmoide para activación
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

# RECORDATORIO: neurona con entradas, pesos y sesgo
def neurona(entradas, pesos, sesgo):
    suma = sum(entrada * peso for entrada, peso in zip(entradas, pesos)) + sesgo  # sumatoria ponderada
    salida = sigmoide(suma)  # aplicamos función de activación
    return salida

# RECORDATORIO: ejemplo simple usando compuerta lógica OR
# Entradas binarias
datos = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1),
]

# RECORDATORIO: pesos y sesgo definidos manualmente para simular una compuerta OR
pesos = [5.0, 5.0]
sesgo = -2.0

# Probar todas las entradas
print("Simulación de neurona (Compuerta OR):")
for entradas, salida_esperada in datos:
    salida_real = neurona(entradas, pesos, sesgo)
    print(f"Entrada: {entradas} → Salida: {round(salida_real)} (Esperado: {salida_esperada})")
