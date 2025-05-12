## Probabilidad a Priori es una estimación inicial de la probabilidad de un evento antes de observar cualquier evidencia.
## f(x) = P(x), donde P representa el conocimiento previo sobre la distribución de los eventos posibles.

# RECORDATORIO: no necesito importar librerías para este ejemplo, todo se hace con diccionarios simples.

# RECORDATORIO: estas son las máquinas que producen los productos.
maquinas = ['M1', 'M2', 'M3']

# RECORDATORIO: esto es lo que sé *antes* de ver cualquier producto. Son mis creencias iniciales.
P_maquina = {
    'M1': 0.5,   # M1 produce la mitad de los productos
    'M2': 0.3,   # M2 produce el 30%
    'M3': 0.2    # M3 produce el 20%
}

# RECORDATORIO: esto es la probabilidad de que un producto salga defectuoso según la máquina.
P_defecto_dado_maquina = {
    'M1': 0.01,  # M1 tiene 1% de defectos
    'M2': 0.03,  # M2 tiene 3%
    'M3': 0.07   # M3 tiene 7%
}

# RECORDATORIO: aquí estoy aplicando la Regla de la Probabilidad Total.
# Sumo la probabilidad de defecto para cada máquina, multiplicada por su frecuencia de producción.
P_defecto = sum(P_defecto_dado_maquina[m] * P_maquina[m] for m in maquinas)

# RECORDATORIO: este es el resultado de la probabilidad total de que un producto cualquiera esté defectuoso.
print(f"\nProbabilidad total de que un producto sea defectuoso: {P_defecto:.4f}")

# RECORDATORIO: esto es lo que sabía *antes* de ver el defecto.
# Son mis probabilidades a priori: lo que creo sin evidencia.
print("\nDistribución de probabilidad a priori:")
for m in maquinas:
    print(f"P({m}) = {P_maquina[m]:.2f}")
