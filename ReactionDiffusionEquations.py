import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de reacción-difusión (Ecuación de Fisher-KPP)
def fisher_kpp(t, u, Du, k):
    dudt = Du * u * (1 - u) - k * u
    return dudt

# Parámetros y condiciones iniciales
Du = 0.1  # Coeficiente de difusión
k = 0.05  # Tasa de reacción
u0 = 0.1  # Condición inicial de la especie

# Tiempo de integración
t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)

# Resolver las ecuaciones de reacción-difusión
sol = solve_ivp(fisher_kpp, t_span, [u0], args=(Du, k), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Concentración de la Especie')
plt.title('Propagación de la Especie (Ecuación de Fisher-KPP)')
plt.grid(True)
plt.show()
