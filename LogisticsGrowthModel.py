import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir la ecuación diferencial logística
def logistic_growth(t, N, r, K):
    dNdt = r * N * (1 - N / K)
    return dNdt

# Parámetros y condiciones iniciales
r = 0.1  # Tasa de crecimiento intrínseca
K = 1000  # Capacidad de carga del entorno
N0 = 10  # Población inicial

# Tiempo de integración
t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)

# Resolver la ecuación diferencial logística
sol = solve_ivp(logistic_growth, t_span, [N0], args=(r, K), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Crecimiento Logístico de una Población')
plt.grid(True)
plt.show()
