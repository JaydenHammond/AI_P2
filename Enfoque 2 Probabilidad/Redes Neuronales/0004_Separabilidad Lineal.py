## Separabilidad Lineal: un conjunto es linealmente separable si existe una línea (o plano) que divide perfectamente dos clases.
## Objetivo: Comprobar si se puede separar un conjunto de datos con una función lineal.

# Recordatorio: cada punto es una tupla (x, y) y tiene una clase (+1 o -1)
datos = [
    ((1, 2), 1),
    ((2, 3), 1),
    ((3, 3), -1),
    ((4, 5), -1)
]

# Recordatorio: esta función simula un clasificador lineal simple: w1*x + w2*y + b
def clasifica(punto, w, b):
    x, y = punto
    resultado = w[0]*x + w[1]*y + b
    return 1 if resultado >= 0 else -1

# Parámetros del modelo (pesos y sesgo)
w = [-1, 1]  # Recordatorio: intentamos con una línea como x = y
b = 0

# Verificar si todos los puntos son clasificados correctamente
separable = True
for (punto, clase_verdadera) in datos:
    clase_predicha = clasifica(punto, w, b)
    print(f"Punto {punto}: Esperado = {clase_verdadera}, Predicho = {clase_predicha}")
    if clase_predicha != clase_verdadera:
        separable = False

# Resultado final
if separable:
    print("\n El conjunto es linealmente separable con esta línea.")
else:
    print("\n El conjunto NO es linealmente separable con esta línea.")
