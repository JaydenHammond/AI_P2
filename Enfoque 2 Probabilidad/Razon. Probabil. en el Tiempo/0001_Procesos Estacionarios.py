## Procesos Estacionarios son aquellos cuyas propiedades estadísticas (media, varianza, autocovarianza) no cambian con el tiempo.
## f(τ) = Cov(Xₜ, Xₜ₊ₜₐᵤ), que depende solo del retraso τ, y E[Xₜ] = µ, Var[Xₜ] = σ² constantes.

import random
import statistics

# RECORDATORIO: Parámetros del proceso AR(1)
phi = 0.7           # coeficiente de autoregresión |φ|<1 garantiza estacionariedad
sigma_ruido = 1.0   # desviación estándar del ruido blanco

# RECORDATORIO: Longitud de la simulación
N = 1000

# RECORDATORIO: Generamos la serie AR(1)
serie = [0.0]  # X₀ = 0
for t in range(1, N):
    # ruido ~ Normal(0, σ²), aproximado por sumas de uniformes
    ruido = sigma_ruido * (random.random() - 0.5 + random.random() - 0.5)
    X_t = phi * serie[-1] + ruido
    serie.append(X_t)

# RECORDATORIO: Calculo de estadísticos para verificar estacionariedad
media = statistics.mean(serie)
varianza = statistics.pvariance(serie)

# RECORDATORIO: Función de autocovarianza empírica para retraso k
def autocovarianza(data, k):
    n = len(data)
    µ = statistics.mean(data)
    return sum((data[i] - µ) * (data[i+k] - µ) for i in range(n - k)) / n

# RECORDATORIO: Calculo autocovarianzas para algunos retrasos
lags = [1, 5, 10]
autocovs = {k: autocovarianza(serie, k) for k in lags}

# RESULTADOS
print(f"\nEstadísticos del proceso AR(1) simulado (N={N}):")
print(f"Media empírica: {media:.3f}")
print(f"Varianza empírica: {varianza:.3f}")
for k in lags:
    print(f"Autocovarianza a retraso {k}: {autocovs[k]:.3f}")
