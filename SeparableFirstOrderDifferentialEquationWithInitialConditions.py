import numpy as np
import matplotlib.pyplot as plt

# Función para la solución de la ecuación diferencial
def y_solution(x):
    return np.exp(0.5 * x**2)

# Valores de x para graficar
x_values = np.linspace(-2, 2, 100)

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_solution(x_values), label='Solución $y(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la Ecuación Diferencial Separable con Condición Inicial')
plt.grid(True)
plt.legend()
plt.show()
