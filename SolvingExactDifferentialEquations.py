import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir las variables y la función potencial
x, y = sp.symbols('x y')
C = sp.symbols('C')
Psi = x**2 * y + x * y**2

# Expresar la solución en términos de C
solution = sp.Eq(Psi, C)
print(f"Solución general: {solution}")

# Convertir la solución simbólica a una función numérica para graficar
Psi_func = sp.lambdify((x, y), Psi, 'numpy')

# Crear una cuadrícula de valores para x e y
x_vals = np.linspace(-5, 5, 400)
y_vals = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = Psi_func(X, Y)

# Graficar las curvas de nivel para diferentes valores de C
plt.figure(figsize=(10, 6))
CS = plt.contour(X, Y, Z, levels=np.linspace(-50, 50, 10), cmap='viridis')
plt.clabel(CS, inline=True, fontsize=8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Soluciones de la ecuación diferencial exacta $(2xy + y^2)dx + (x^2 + 2xy)dy = 0$')
plt.grid(True)
plt.show()
