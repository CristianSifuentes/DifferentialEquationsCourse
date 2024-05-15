import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir las variables y la función
x = sp.symbols('x')
C = sp.symbols('C')
y = sp.Function('y')(x)

# Definir la ecuación diferencial
ode = sp.Eq(y.diff(x) - (1/x)*y, x**2)

# Resolver la ecuación diferencial
solution = sp.dsolve(ode, y)
y_sol = solution.rhs

# Mostrar la solución general
print(f"Solución general: y = {y_sol}")

# Convertir la solución simbólica a una función numérica
# Simplificar la expresión para asegurar que pueda ser evaluada numéricamente.
y_sol_simplified = sp.simplify(y_sol)
y_func = sp.lambdify((x, C), y_sol_simplified, modules=['numpy'])

# Definir un rango de valores para x, evitando el punto singular x=0
x_vals = np.linspace(1, 10, 400)

# Elegir un valor arbitrario para la constante de integración
C_val = 1  # Puedes cambiar este valor para ver cómo cambia la solución

# Calcular los valores de y para los valores de x dados
y_vals = y_func(x_vals, C_val)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'C = {C_val}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la ecuación diferencial $\\frac{dy}{dx} - \\frac{y}{x} = x^2$')
plt.legend()
plt.grid(True)
plt.show()
