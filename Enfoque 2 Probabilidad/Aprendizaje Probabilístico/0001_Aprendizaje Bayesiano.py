## Aprendizaje Bayesiano actualiza parámetros de un modelo probabilístico usando evidencia nueva de manera recursiva.
## f(θ | data) ∝ P(data | θ) · P(θ), aquí usamos una distribución Beta para estimar la probabilidad de éxito de una moneda.

import random

# RECORDATORIO: no necesitamos librerías externas; trabajamos con conteos simples.

# RECORDATORIO: definimos la prior Beta(α, β) para la probabilidad θ de "Cara".
alpha_prior = 2   # α > 1 favorece sesgo hacia éxito inicial
beta_prior  = 2   # β > 1 favorece sesgo hacia fracaso inicial

# RECORDATORIO: datos observados: lanzamientos de moneda (1=Cara, 0=Cruz)
datos = [1, 0, 1, 1, 0, 1, 0, 1]  # 8 lanzamientos

# RECORDATORIO: contamos éxitos y fracasos
exitos = sum(datos)
fracasos = len(datos) - exitos

# RECORDATORIO: actualizamos la posterior Beta(α+éxitos, β+fracasos)
alpha_post = alpha_prior + exitos
beta_post  = beta_prior  + fracasos

# RECORDATORIO: calculamos la media posterior como estimador de θ
theta_estimada = alpha_post / (alpha_post + beta_post)

# RESULTADOS
print("Aprendizaje Bayesiano (Beta-Binomial):")
print(f"Prior   → α = {alpha_prior}, β = {beta_prior}")
print(f"Datos   → éxitos = {exitos}, fracasos = {fracasos}")
print(f"Posterior → α' = {alpha_post}, β' = {beta_post}")
print(f"Estimador de θ (media posterior) = {theta_estimada:.3f}")
