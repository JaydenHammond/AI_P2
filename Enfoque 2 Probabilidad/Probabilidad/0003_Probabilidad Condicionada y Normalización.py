## Probabilidad Condicionada y Normalización calcula la probabilidad de un evento dado otro y ajusta la distribución para que sume 1.
## f(A|B) = P(A ∧ B) / P(B); después normalizo para asegurar que la suma de todas las probabilidades condicionadas sea 1.

import random

# RECORDATORIO: Defino dos eventos simples, por ejemplo, lanzar una moneda y un dado.
eventos = ['Cara', 'Sello']
resultados_dado = [1, 2, 3, 4, 5, 6]

# RECORDATORIO: P(Cara) = 0.5, P(Sello) = 0.5 (moneda justa).
P_moneda = {e: 0.5 for e in eventos}

# RECORDATORIO: P(número par | Cara) y P(número par | Sello): supongamos que el dado está sesgado según la moneda.
P_dado_dado_moneda = {
    'Cara': {n: (1/3 if n % 2 == 0 else (2/3) / 3) for n in resultados_dado},
    # RECORDATORIO: si salió Cara, el dado favorece pares (1/3 total para pares, distribuido entre 3 pares).
    'Sello': {n: (2/3 if n % 2 == 0 else (1/3) / 3) for n in resultados_dado}
    # RECORDATORIO: si salió Sello, el dado favorece impares (2/3 total para impares, distribuido entre 3 impares).
}

# RECORDATORIO: Queremos P(moneda = Cara | dado muestra un par).
# Primero calculo P(dado = par ∧ moneda = Cara) = P(Cara) * P(dado = par | Cara).
P_conjunta = {}
for e in eventos:
    P_conjunta[e] = P_moneda[e] * sum(P_dado_dado_moneda[e][n] for n in resultados_dado if n % 2 == 0)

# RECORDATORIO: P(dado = par) = suma de todas P_conjunta para eventos Cara y Sello.
P_par = sum(P_conjunta.values())

# RECORDATORIO: Ahora la probabilidad condicionada: P(Cara ∧ par) / P(par), y similar para Sello.
P_condicional = {e: P_conjunta[e] / P_par for e in eventos}

# RECORDATORIO: Al calcular así ya estoy normalizando, porque divido por la suma total P_par.
# Apunto la distribución final P(moneda | par).
print("\nProbabilidad condicionada P(moneda | dado es par):")
for e in eventos:
    print(f"P({e} | Par) = {P_condicional[e]:.2f}")
