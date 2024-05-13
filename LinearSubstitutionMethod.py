import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
def differential_equation(x, v):
    return v - 2 * x * v

# Resolver la ecuación diferencial
x_span = (-2, 2)
v0 = 1  # Supongamos una condición inicial
sol = solve_ivp(differential_equation, x_span, [v0], t_eval=np.linspace(-2, 2, 100))

# Obtener la solución v(x)
v_solution = sol.y[0]

# Calcular y(x)
y_solution = v_solution * np.exp(sol.t**2)

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, y_solution, label='Solución $y(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la Ecuación Diferencial Lineal con Método de Sustitución Lineal')
plt.grid(True)
plt.legend()
plt.show()
