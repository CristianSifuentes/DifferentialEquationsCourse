import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de Brusselator
def brusselator(t, y, a, b):
    dydt = [1 - (b + 1) * y[0] + a * y[0]**2 * y[1], 
            b * y[0] - a * y[0]**2 * y[1]]
    return dydt

# Parámetros y condiciones iniciales
a = 1.0
b = 3.0
y0 = [1.0, 1.0]

# Tiempo de integración
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Resolver las ecuaciones de Brusselator
sol = solve_ivp(brusselator, t_span, y0, args=(a, b), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='u')
plt.plot(sol.t, sol.y[1], label='v')
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Solución de las Ecuaciones de Brusselator')
plt.legend()
plt.grid(True)
plt.show()
