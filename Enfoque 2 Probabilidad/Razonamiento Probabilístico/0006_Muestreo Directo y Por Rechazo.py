## Muestreo Directo y Por Rechazo genera muestras de una distribución objetivo usando dos enfoques distintos.
## Directo: aplica la inversión de la CDF; Por Rechazo: usa una propuesta fácil y acepta/descarta según densidades.

# RECORDATORIO: import random para generar números aleatorios uniformes.
import random
# RECORDATORIO: import math para acceso a funciones matemáticas (aquí podrías usar sqrt, log, etc.).
import math

# RECORDATORIO: Defino la distribución objetivo en [0,1] con densidad f(x) = 3·x^2 (Beta(3,1)).
# Esta densidad ya está normalizada (∫₀¹3x²dx = 1).
def f_objetivo(x):
    return 3 * x**2

# Muestreo Directo usando inversa de la CDF:
# CDF F(x)=x^3 => inversa F⁻¹(u)=u^(1/3)
def muestreo_directo(N):
    muestras = []
    for _ in range(N):
        # RECORDATORIO: random.random() devuelve un flotante en [0,1).
        u = random.random()
        # RECORDATORIO: elevamos a 1/3 para invertir la CDF.
        x = u ** (1/3)
        muestras.append(x)
    return muestras

# Muestreo Por Rechazo usando propuesta uniforme en [0,1]:
# f_propuesta(x)=1 en [0,1]; M = max f_objetivo = f_objetivo(1) = 3
def muestreo_rechazo(N):
    muestras = []
    M = 3.0  # RECORDATORIO: cota superior para f_objetivo(x)/f_propuesta(x).
    while len(muestras) < N:
        # RECORDATORIO: propongo x desde uniforme[0,1].
        x = random.random()
        # RECORDATORIO: u·M compara con la densidad objetivo en x.
        u = random.random()
        if u * M <= f_objetivo(x):
            muestras.append(x)  # RECORDATORIO: acepto x si cumple la condición.
        # else: descarto y vuelvo a proponer
    return muestras

# Ejecución de muestreo
N = 10000
directas = muestreo_directo(N)
rechazo = muestreo_rechazo(N)

# RECORDATORIO: calcular promedio de muestras para comparar con valor teórico E[X] = 3/4 = 0.75
promedio_directo = sum(directas) / N
promedio_rechazo = sum(rechazo) / N

# RESULTADOS
print("\nMuestreo Directo → promedio ≈", round(promedio_directo, 3))
print("Muestreo Por Rechazo → promedio ≈", round(promedio_rechazo, 3))
