import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir las variables
x, y, C = sp.symbols('x y C')

# Solución de la ecuación diferencial
solution = sp.Eq(y**2, 2 * x**2 * (sp.ln(sp.Abs(x)) + C))

# Mostrar la solución general
print(f"Solución general: {solution}")

# Convertir la solución simbólica a una función numérica para graficar
y_expr = sp.solve(solution, y)
y_func_pos = sp.lambdify((x, C), y_expr[0], 'numpy')
y_func_neg = sp.lambdify((x, C), y_expr[1], 'numpy')

# Definir un rango de valores para x
x_vals = np.linspace(0.1, 10, 400)

# Elegir un valor arbitrario para la constante de integración
C_val = 1  # Puedes cambiar este valor para ver cómo cambia la solución

# Calcular los valores de y para los valores de x dados
y_vals_pos = y_func_pos(x_vals, C_val)
y_vals_neg = y_func_neg(x_vals, C_val)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals_pos, label=f'C = {C_val}, y > 0')
plt.plot(x_vals, y_vals_neg, label=f'C = {C_val}, y < 0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la ecuación diferencial homogénea')
plt.legend()
plt.grid(True)
plt.show()
