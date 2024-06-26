'''

¡Claro! Podemos crear un ejemplo utilizando la ecuación diferencial del oscilador armónico amortiguado y 
luego visualizar la solución utilizando el módulo matplotlib para graficar. Aquí tienes un ejemplo:
'''


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la ecuación diferencial del oscilador amortiguado
def oscillator(y, t, omega0, gamma):
    """
    y[0] = posición
    y[1] = velocidad
    """
    dydt = [y[1], -2 * gamma * y[1] - omega0**2 * y[0]]
    return dydt

# Parámetros del oscilador
omega0 = 2 * np.pi  # Frecuencia angular
gamma = 0.1  # Factor de amortiguamiento

# Condiciones iniciales
y0 = [1.0, 0.0]  # Posición inicial = 1, velocidad inicial = 0

# Tiempo
t = np.linspace(0, 10, 1000)

# Resolver la ecuación diferencial
sol = odeint(oscillator, y0, t, args=(omega0, gamma))

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(t, sol[:, 0], label='Posición')
plt.plot(t, sol[:, 1], label='Velocidad')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Solución del Oscilador Amortiguado')
plt.legend()
plt.grid(True)
plt.show()


'''
Este código define la ecuación diferencial del oscilador amortiguado, resuelve la ecuación usando odeint de SciPy, y luego utiliza matplotlib para graficar la posición y la velocidad en función del tiempo.

¿Te gustaría profundizar en algún aspecto de este ejemplo o necesitas más explicaciones sobre alguna parte del código?
'''