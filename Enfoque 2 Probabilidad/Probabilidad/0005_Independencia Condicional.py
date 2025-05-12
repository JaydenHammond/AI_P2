## Independencia Condicional verifica que dos variables sean independientes dado una tercera, es decir, P(X, Y | Z) = P(X | Z)·P(Y | Z).
## f(n) = indicador booleano; comprueba para todas las combinaciones si se cumple la igualdad.

import itertools

# RECORDATORIO: Defino los posibles valores de cada variable.
valores_X = ['x1', 'x2']
valores_Y = ['y1', 'y2']
valores_Z = ['z1', 'z2']

# RECORDATORIO: Distribución a priori de Z.
P_Z = {'z1': 0.6, 'z2': 0.4}

# RECORDATORIO: Distribuciones condicionales P(X|Z) y P(Y|Z).
P_X_given_Z = {
    'z1': {'x1': 0.7, 'x2': 0.3},
    'z2': {'x1': 0.4, 'x2': 0.6}
}
P_Y_given_Z = {
    'z1': {'y1': 0.5, 'y2': 0.5},
    'z2': {'y1': 0.2, 'y2': 0.8}
}

# RECORDATORIO: Genero la distribución conjunta P(X,Y,Z) asumiendo independencia condicional.
P_XYZ = {}
for z in valores_Z:
    for x in valores_X:
        for y in valores_Y:
            P_XYZ[(x, y, z)] = P_Z[z] * P_X_given_Z[z][x] * P_Y_given_Z[z][y]

# RECORDATORIO: Función para calcular P(X,Y|Z = z).
def P_XY_given_z(x, y, z):
    # P(X, Y | Z=z) = P(X,Y,Z) / P(Z)
    return P_XYZ[(x, y, z)] / P_Z[z]

# RECORDATORIO: Función para calcular P(X|Z=z)·P(Y|Z=z).
def P_X_given_z_times_P_Y_given_z(x, y, z):
    return P_X_given_Z[z][x] * P_Y_given_Z[z][y]

# RECORDATORIO: Verifico la independencia condicional en todas las combinaciones.
cumple = True
for z in valores_Z:
    for x, y in itertools.product(valores_X, valores_Y):
        p_xy_z = P_XY_given_z(x, y, z)
        p_prod  = P_X_given_z_times_P_Y_given_z(x, y, z)
        # RECORDATORIO: comparo con un pequeño margen de error.
        if abs(p_xy_z - p_prod) > 1e-8:
            cumple = False
            print(f"Falla en ({x},{y}|{z}): P={p_xy_z:.4f} vs P*P={p_prod:.4f}")

# RESULTADO: Muestro si la independencia condicional se cumple.
if cumple:
    print("\nTodas las combinaciones cumplen P(X,Y|Z) = P(X|Z)·P(Y|Z).")
else:
    print("\nNo todas las combinaciones cumplen la independencia condicional.")
