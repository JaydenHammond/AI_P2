## Aprendizaje Profundo (Deep Learning) implementa una red neuronal multicapa simple desde cero.
## f(x) = softmax(W₂·ReLU(W₁·x + b₁) + b₂); entrenamos con descenso de gradiente y propagación hacia atrás.

import random
import math

# RECORDATORIO: inicializar semilla para reproducibilidad
random.seed(42)

# RECORDATORIO: datos de ejemplo (XOR) con etiquetas one-hot
# Entradas de 2 dimensiones
X = [
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0],
]
# Salidas: [1,0] para clase 0, [0,1] para clase 1
Y = [
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
]

# RECORDATORIO: parámetros de la red
n_input = 2
n_hidden = 4
n_output = 2
lr = 0.1     # tasa de aprendizaje
epochs = 1000

# RECORDATORIO: inicializo pesos y biases con valores pequeños aleatorios
def rand_mat(rows, cols):
    return [[random.uniform(-1, 1) * 0.1 for _ in range(cols)] for _ in range(rows)]

W1 = rand_mat(n_hidden, n_input)   # pesos capa oculta
b1 = [0.0] * n_hidden               # bias capa oculta
W2 = rand_mat(n_output, n_hidden)   # pesos capa de salida
b2 = [0.0] * n_output               # bias capa de salida

# RECORDATORIO: funciones de activación y derivadas
def relu(v):
    return [max(0, x) for x in v]

def d_relu(v):
    return [1 if x > 0 else 0 for x in v]

def softmax(v):
    exps = [math.exp(x) for x in v]
    s = sum(exps) or 1e-12
    return [e / s for e in exps]

# RECORDATORIO: producto matriz-vector
def mat_vec_mul(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

# RECORDATORIO: entrenamiento con retropropagación
for ep in range(epochs):
    loss = 0.0
    for x, y_true in zip(X, Y):
        # ---- Forward ----
        z1 = [w + b for w, b in zip(mat_vec_mul(W1, x), b1)]   # RECORDATORIO: pre-activación capa oculta
        a1 = relu(z1)                                          # RECORDATORIO: activación ReLU
        z2 = [w + b for w, b in zip(mat_vec_mul(W2, a1), b2)]  # RECORDATORIO: pre-activación salida
        a2 = softmax(z2)                                       # RECORDATORIO: salida softmax
        
        # ---- Loss ----
        loss += -sum(y_true[i] * math.log(a2[i] + 1e-12) for i in range(n_output))
        
        # ---- Backward ----
        # error salida
        delta2 = [a2[i] - y_true[i] for i in range(n_output)]               # RECORDATORIO: dL/dz2
        # gradientes W2, b2
        dW2 = [[delta2[i] * a1[j] for j in range(n_hidden)] for i in range(n_output)]
        db2 = delta2[:]
        # error capa oculta
        d1 = d_relu(z1)                                                     # RECORDATORIO: dReLU
        delta1 = [d1[j] * sum(W2[i][j] * delta2[i] for i in range(n_output))
                  for j in range(n_hidden)]                                 # RECORDATORIO: dL/dz1
        # gradientes W1, b1
        dW1 = [[delta1[j] * x[k] for k in range(n_input)] for j in range(n_hidden)]
        db1 = delta1[:]
        
        # ---- Actualizar parámetros ----
        for i in range(n_output):
            for j in range(n_hidden):
                W2[i][j] -= lr * dW2[i][j]
            b2[i]    -= lr * db2[i]
        for j in range(n_hidden):
            for k in range(n_input):
                W1[j][k] -= lr * dW1[j][k]
            b1[j]    -= lr * db1[j]
    
    # RECORDATORIO: imprimir pérdida cada 200 épocas
    if ep % 200 == 0:
        print(f"Epoca {ep}, Loss: {loss/len(X):.4f}")

# RECORDATORIO: prueba final
print("\nPruebas finales de la red entrenada:")
for x in X:
    # forward
    a1 = relu([w + b for w, b in zip(mat_vec_mul(W1, x), b1)])
    a2 = softmax([w + b for w, b in zip(mat_vec_mul(W2, a1), b2)])
    pred = a2.index(max(a2))
    print(f"Entrada {x} → Clase predicha: {pred}")
