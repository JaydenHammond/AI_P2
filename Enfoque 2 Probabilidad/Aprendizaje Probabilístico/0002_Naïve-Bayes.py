## Naïve-Bayes entrena un clasificador probabilístico asumiendo independencia condicional de características.
## f(c | x) ∝ P(c) × ∏ P(xᵢ | c); elige la clase c con mayor probabilidad posterior.

# RECORDATORIO: usamos solo diccionarios y contadores, sin librerías externas.

# Datos de entrenamiento: mensajes y su etiqueta ('spam' o 'ham')
datos_train = [
    ("Gana dinero rápido ahora",      "spam"),
    ("Oferta exclusiva, haz clic",    "spam"),
    ("Reunión a las 10am mañana",     "ham"),
    ("¿Quieres almorzar juntos?",     "ham"),
    ("Descuento en tu próxima compra","spam"),
    ("Proyecto de IA vence hoy",      "ham")
]

# RECORDATORIO: vocabulario y conteos por clase
vocab = set()
conteo_palabras = {"spam": {}, "ham": {}}
conteo_clases   = {"spam": 0,   "ham": 0}

# Entrenamiento: calcular priors y likelihoods (frecuencias)
for texto, clase in datos_train:
    conteo_clases[clase] += 1                      # RECORDATORIO: sumo al conteo de documentos
    for palabra in texto.lower().split():
        vocab.add(palabra)                         # RECORDATORIO: construyo vocabulario
        conteo_palabras[clase][palabra] = conteo_palabras[clase].get(palabra, 0) + 1

total_docs = sum(conteo_clases.values())

# RECORDATORIO: función para clasificar un mensaje nuevo
def clasificar_nb(texto):
    palabras = texto.lower().split()
    mejor_clase, mejor_log_prob = None, float('-inf')
    for clase in conteo_clases:
        # RECORDATORIO: log P(c)
        log_prob = math.log(conteo_clases[clase] / total_docs)
        # RECORDATORIO: sumar log P(palabra | clase) con suavizado Laplace
        N_clase = sum(conteo_palabras[clase].values())
        V = len(vocab)
        for p in palabras:
            count = conteo_palabras[clase].get(p, 0)
            # Laplace: (count+1)/(N_clase+V)
            log_prob += math.log((count + 1) / (N_clase + V))
        if log_prob > mejor_log_prob:
            mejor_log_prob, mejor_clase = log_prob, clase
    return mejor_clase

# RECORDATORIO: no olvides importar math para logaritmos
import math

nuevos = [
    "haz clic para ganar dinero",
    "¿vamos al proyecto de IA?",
    "descuento exclusivo hoy"
]

for msg in nuevos:
    etiqueta = clasificar_nb(msg)
    print(f"Mensaje: '{msg}' → Clasificado como: {etiqueta}")
