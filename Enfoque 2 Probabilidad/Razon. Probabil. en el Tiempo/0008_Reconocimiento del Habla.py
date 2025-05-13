## Reconocimiento del Habla usa un enfoque de plantillas simples para comparar características de audio y decidir la palabra más parecida.
## f(sample) = argmin_word ∥features(sample) − template_features(word)∥²

import random

# RECORDATORIO: simulamos extracción de características de un fragmento de audio como lista de valores.
def extraer_caracteristicas(audio):
    # RECORDATORIO: en la práctica usarías MFCC, aquí devolvemos 13 coeficientes aleatorios.
    return [random.uniform(0, 1) for _ in range(13)]

# RECORDATORIO: plantillas de características para cada palabra conocida
plantillas = {
    'hola':   [0.2, 0.1, 0.5, 0.7, 0.3, 0.6, 0.4, 0.8, 0.2, 0.1, 0.5, 0.7, 0.3],
    'adios':  [0.6, 0.4, 0.2, 0.1, 0.8, 0.3, 0.7, 0.5, 0.9, 0.2, 0.4, 0.6, 0.1],
    'gracias':[0.3, 0.7, 0.4, 0.2, 0.6, 0.8, 0.1, 0.5, 0.3, 0.9, 0.2, 0.4, 0.6]
}

# RECORDATORIO: calcula distancia euclidiana al cuadrado entre dos vectores
def distancia_cuadrada(v1, v2):
    return sum((a - b)**2 for a, b in zip(v1, v2))

# RECORDATORIO: función principal de reconocimiento
def reconocer_palabra(audio):
    # RECORDATORIO: extraigo características de la señal de audio
    feats = extraer_caracteristicas(audio)
    # RECORDATORIO: inicializo mejor palabra con infinito
    mejor_palabra, mejor_dist = None, float('inf')
    # RECORDATORIO: comparo con cada plantilla y elijo la más cercana
    for palabra, tpl in plantillas.items():
        dist = distancia_cuadrada(feats, tpl)
        if dist < mejor_dist:
            mejor_dist, mejor_palabra = dist, palabra
    return mejor_palabra

# RECORDATORIO: 'audio_real' representaría los datos de audio; aquí es sólo un marcador.
audio_real = 'datos_de_audio_simulado'
resultado = reconocer_palabra(audio_real)

print(f"Palabra reconocida: {resultado}")
