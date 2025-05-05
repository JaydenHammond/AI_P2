## Valor de la Información (VOI) mide cuánto mejora la decisión óptima si se obtiene información adicional antes de actuar.
## f(n) = U_con_info - U_sin_info; se evalúa si vale la pena pagar por conocer un estado incierto antes de decidir.

# Estados posibles del clima
estados = ['Lluvia', 'Soleado']

# Acciones posibles para un evento
acciones = ['Hacer evento al aire libre', 'Hacer evento bajo techo']

# Probabilidades iniciales sin información
probabilidades = {
    'Lluvia': 0.4,
    'Soleado': 0.6
}
# Utilidades sin información adicional
utilidades = {
    'Hacer evento al aire libre': {'Lluvia': -10, 'Soleado': 10},
    'Hacer evento bajo techo': {'Lluvia': 5, 'Soleado': 5}
}
# Función para calcular utilidad esperada sin información
def utilidad_esperada(prob, accion):
    return sum(prob[estado] * utilidades[accion][estado] for estado in estados)

# Mejor acción sin información
utilidades_sin_info = {accion: utilidad_esperada(probabilidades, accion) for accion in acciones}
mejor_sin_info = max(utilidades_sin_info, key=utilidades_sin_info.get)
u_sin_info = utilidades_sin_info[mejor_sin_info]

# Con información perfecta: sabemos con certeza si lloverá o no
u_con_info = 0
for estado in estados:
    # Dado ese estado, elegimos la mejor acción
    mejor_accion_estado = max(acciones, key=lambda a: utilidades[a][estado])
    u_con_info += probabilidades[estado] * utilidades[mejor_accion_estado][estado]
valor_informacion = u_con_info - u_sin_info

print("\nAnálisis de Valor de la Información (VOI):")
print(f"Mejor acción sin información: {mejor_sin_info} (Utilidad esperada: {u_sin_info:.2f})")
print(f"Utilidad esperada con información perfecta: {u_con_info:.2f}")
print(f"Valor de la Información: {valor_informacion:.2f}")
