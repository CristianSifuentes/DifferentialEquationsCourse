import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de Van der Pol
def van_der_pol(t, y, mu):
    dydt = [y[1], mu * (1 - y[0]**2) * y[1] - y[0]]
    return dydt

# Parámetros y condiciones iniciales
mu = 1.0
y0 = [1.0, 0.0]

# Tiempo de integración
t_span = (0, 20)
t_eval = np.linspace(0, 20, 1000)

# Resolver las ecuaciones de Van der Pol
sol = solve_ivp(van_der_pol, t_span, y0, args=(mu,), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Solución de las Ecuaciones de Van der Pol')
plt.grid(True)
plt.show()