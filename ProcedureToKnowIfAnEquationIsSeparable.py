import numpy as np
import matplotlib.pyplot as plt

# Función para la solución de la ecuación diferencial
def y_solution(x):
    return 2 * np.sqrt(x**2 / 5)

# Valores de x para graficar
x_values = np.linspace(-5, 5, 100)

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_solution(x_values), label='Solución $y(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la Ecuación Diferencial Separable con Condición Inicial')
plt.grid(True)
plt.legend()
plt.show()
