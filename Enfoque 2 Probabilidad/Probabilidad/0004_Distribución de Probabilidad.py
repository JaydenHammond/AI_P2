## Distribución de Probabilidad define la probabilidad de cada resultado posible de una variable aleatoria discreta.
## f(x) = P(X = x), donde la suma de todas las P(X = x) debe ser 1.

import random

# RECORDATORIO: aquí defino los posibles eventos, por ejemplo colores de una canica en una urna.
colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']

# RECORDATORIO: esta es mi distribución de probabilidad inicial para cada color.
# Asegúrate de que sumen 1.0.
P_color = {
    'Rojo':     0.4,   # 40% de probabilidad de sacar Rojo
    'Azul':     0.3,   # 30% para Azul
    'Verde':    0.2,   # 20% para Verde
    'Amarillo': 0.1    # 10% para Amarillo
}

# RECORDATORIO: compruebo que la distribución está normalizada.
suma_prob = sum(P_color.values())
assert abs(suma_prob - 1.0) < 1e-8, "La distribución no suma 1!"

# RECORDATORIO: función para muestrear un color según la distribución P_color.
def muestrear_color(distribucion):
    r = random.random()  # número en [0,1)
    acumulado = 0.0
    for color, p in distribucion.items():
        acumulado += p
        if r < acumulado:
            return color
    return color  # en caso de redondeo, devuelvo el último

# RECORDATORIO: simulo N extracciones para aproximar la distribución empírica.
N = 10000
conteo = {c: 0 for c in colores}
for _ in range(N):
    c = muestrear_color(P_color)
    conteo[c] += 1

# RECORDATORIO: convierto conteos a frecuencias relativas.
frecuencias = {c: conteo[c] / N for c in colores}

# RESULTADO: muestro la distribución teórica y la empírica obtenida por muestreo.
print("\nDistribución teórica P(color):")
for c in colores:
    print(f"P({c}) = {P_color[c]:.2f}")

print("\nDistribución empírica tras muestreo:")
for c in colores:
    print(f"Freq({c}) ≈ {frecuencias[c]:.2f}")
