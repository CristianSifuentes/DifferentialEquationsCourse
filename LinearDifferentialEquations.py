import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir las variables y la función
x, C = sp.symbols('x C')
y = sp.Function('y')(x)

# Definir la ecuación diferencial
ode = sp.Eq(y.diff(x) + 3*y, 6*x)

# Resolver la ecuación diferencial
solution = sp.dsolve(ode, y)
y_sol = solution.rhs

# Mostrar la solución general
print(f"Solución general: y = {y_sol}")

# Convertir la solución simbólica a una función numérica
y_func = sp.lambdify((x, C), y_sol, modules=['numpy'])

# Definir un rango de valores para x
x_vals = np.linspace(0, 5, 400)

# Elegir un valor arbitrario para la constante de integración
C_val = 1  # Puedes cambiar este valor para ver cómo cambia la solución

# Calcular los valores de y para los valores de x dados
y_vals = y_func(x_vals, C_val)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'C = {C_val}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la ecuación diferencial $\\frac{dy}{dx} + 3y = 6x$')
plt.legend()
plt.grid(True)
plt.show()
