import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de Lorenz
def lorenz(t, y, sigma, rho, beta):
    dydt = [sigma * (y[1] - y[0]), y[0] * (rho - y[2]) - y[1], y[0] * y[1] - beta * y[2]]
    return dydt

# Parámetros y condiciones iniciales
sigma = 10
rho = 28
beta = 8/3
y0 = [1, 1, 1]  # Condiciones iniciales

# Tiempo de integración
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Resolver las ecuaciones de Lorenz
sol = solve_ivp(lorenz, t_span, y0, args=(sigma, rho, beta), t_eval=t_eval)

# Visualizar la solución
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Atractor de Lorenz')
plt.show()
