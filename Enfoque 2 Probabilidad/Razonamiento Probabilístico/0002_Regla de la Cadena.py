## Regla de la Cadena descompone la probabilidad conjunta en una serie de términos condicionales encadenados.
## f(A,B,C) = P(A) × P(B | A) × P(C | A, B); permite calcular P de múltiples eventos ordenados.

import itertools

# RECORDATORIO: Defino eventos simples, por ejemplo, tres pruebas A, B y C, con valores True/False.
eventos = ['A', 'B', 'C']
valores = ['True', 'False']

# RECORDATORIO: P(A) es la probabilidad marginal de A.
P_A = {'True': 0.3, 'False': 0.7}

# RECORDATORIO: P(B | A) para cada valor de A.
P_B_given_A = {
    'True':  {'True': 0.6, 'False': 0.4},
    'False': {'True': 0.2, 'False': 0.8},
}

# RECORDATORIO: P(C | A, B) dado cada combinación de A y B.
P_C_given_AB = {
    ('True',  'True'):  {'True': 0.9, 'False': 0.1},
    ('True',  'False'): {'True': 0.5, 'False': 0.5},
    ('False', 'True'):  {'True': 0.4, 'False': 0.6},
    ('False', 'False'): {'True': 0.1, 'False': 0.9},
}

# RECORDATORIO: Calculo P(A, B, C) usando la Regla de la Cadena.
P_ABC = {}
for a, b, c in itertools.product(valores, repeat=3):
    # Aplico P(A) × P(B|A) × P(C|A,B)
    p = P_A[a]
    p *= P_B_given_A[a][b]
    p *= P_C_given_AB[(a, b)][c]
    P_ABC[(a, b, c)] = p

# RECORDATORIO: Muestro algunas probabilidades conjuntas calculadas.
print("\nAlgunas probabilidades conjuntas P(A, B, C):")
for combo in [('True','True','True'), ('True','False','True'), ('False','True','False')]:
    print(f"P(A={combo[0]}, B={combo[1]}, C={combo[2]}) = {P_ABC[combo]:.4f}")

# RECORDATORIO: Verifico que la suma de todas P(A,B,C) sea aproximadamente 1 (normalización).
suma_total = sum(P_ABC.values())
print(f"\nSuma total de P(A,B,C) = {suma_total:.4f}  # debe ser ≈ 1.0")
