import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la ecuación diferencial de Lotka-Volterra
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    """
    y[0] = presas
    y[1] = depredadores
    """
    prey, predators = y
    dpreydt = alpha * prey - beta * prey * predators
    dpredatordt = delta * prey * predators - gamma * predators
    return [dpreydt, dpredatordt]

# Parámetros del modelo
alpha = 0.1  # Tasa de crecimiento de las presas
beta = 0.02  # Tasa de mortalidad de las presas debido a los depredadores
delta = 0.02  # Tasa de crecimiento de los depredadores debido a las presas
gamma = 0.1  # Tasa de mortalidad de los depredadores

# Condiciones iniciales
y0 = [40, 9]  # Población inicial de presas y depredadores

# Tiempo
t = np.linspace(0, 200, 1000)

# Resolver la ecuación diferencial
sol = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(t, sol[:, 0], label='Presas')
plt.plot(t, sol[:, 1], label='Depredadores')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Dinámica de Presas y Depredadores (Lotka-Volterra)')
plt.legend()
plt.grid(True)
plt.show()
