## Filtro de Kalman con Control en Python puro (corrección para inversión de matriz 1×1).
## f(x̂, P) = (predict → update con control u), corrige la inversión de S cuando es escalar.

import random
import math

# RECORDATORIO: intervalo de tiempo
dt = 1.0

# RECORDATORIO: Matriz de transición A para estado [pos, vel]
A = [[1, dt],
     [0, 1 ]]

# RECORDATORIO: Matriz de control B para entrada u = aceleración
B = [[0.5 * dt**2],
     [dt]]

# RECORDATORIO: Observamos solo la posición
H = [[1, 0]]

# RECORDATORIO: Covarianza de ruido de proceso Q
sigma_process = 0.2
Q = [[(dt**4)/4 * sigma_process, (dt**3)/2 * sigma_process],
     [(dt**3)/2 * sigma_process, dt**2 * sigma_process]]

# RECORDATORIO: Covarianza de ruido de medición R (1×1)
sigma_measure = 2.0
R = [[sigma_measure]]

# RECORDATORIO: Estado inicial x̂₀ = [posición, velocidad]
x_hat = [0.0, 0.0]
# RECORDATORIO: Covarianza inicial P₀ (incertidumbre grande)
P = [[1000.0,    0.0],
     [   0.0, 1000.0]]

def mat_mul(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_transpose(M):
    return list(map(list, zip(*M)))

def mat_mat_mul(A, B):
    BT = mat_transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in BT] for row in A]

def mat_inv(M):
    # RECORDATORIO: invierte matrices 1×1 o 2×2
    n = len(M)
    if n == 1:
        # RECORDATORIO: S es escalar → inverso es 1/elemento
        return [[1.0 / M[0][0]]]
    # RECORDATORIO: caso 2×2
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    return [[ M[1][1]/det, -M[0][1]/det],
            [-M[1][0]/det,  M[0][0]/det]]

def kalman_step(x_prev, P_prev, z, u):
    # Predict con control u
    x_pred = [
        A[0][0]*x_prev[0] + A[0][1]*x_prev[1] + B[0][0]*u,
        A[1][0]*x_prev[0] + A[1][1]*x_prev[1] + B[1][0]*u
    ]
    P_pred = mat_add(mat_mat_mul(mat_mat_mul(A, P_prev), mat_transpose(A)), Q)

    # S = H·P_pred·Hᵀ + R (1×1)
    S = mat_add(mat_mat_mul(mat_mat_mul(H, P_pred), mat_transpose(H)), R)
    # RECORDATORIO: usar mat_inv que maneja 1×1
    S_inv = mat_inv(S)
    # Kalman gain K = P_pred·Hᵀ·S⁻¹ → P_pred(2×2)·Hᵀ(2×1) = 2×1, luego escala por S_inv[0][0]
    PHt = mat_mat_mul(P_pred, mat_transpose(H))
    K = [[PHt[i][0] * S_inv[0][0]] for i in range(2)]

    # Update
    y = z - (H[0][0]*x_pred[0] + H[0][1]*x_pred[1])  # innovación
    x_upd = [x_pred[i] + K[i][0]*y for i in range(2)]
    I = [[1,0],[0,1]]
    KH = mat_mat_mul(K, H)
    P_upd = mat_mat_mul(mat_sub(I, KH), P_pred)

    return x_upd, P_upd


true_state = [0.0, 1.0]
u = 0.5
measurements = []
N = 10

for _ in range(N):
    # evolución real con ruido de proceso
    true_state = [
        A[0][0]*true_state[0] + A[0][1]*true_state[1] + B[0][0]*u + random.gauss(0, math.sqrt(sigma_process)),
        A[1][0]*true_state[0] + A[1][1]*true_state[1] + B[1][0]*u + random.gauss(0, math.sqrt(sigma_process))
    ]
    # medición de posición con ruido
    z = true_state[0] + random.gauss(0, math.sqrt(sigma_measure))
    measurements.append(z)

estimates = []
for z in measurements:
    x_hat, P = kalman_step(x_hat, P, z, u)
    estimates.append((x_hat[0], x_hat[1]))

# RESULTADOS
print("\nFiltro de Kalman con Control (corregido):")
for i, (z, (pos, vel)) in enumerate(zip(measurements, estimates), 1):
    print(f"Paso {i}: Medición pos={z:.2f}, Estimación pos={pos:.2f}, vel={vel:.2f}")
