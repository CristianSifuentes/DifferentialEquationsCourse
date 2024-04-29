import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de FitzHugh-Nagumo
def fitzhugh_nagumo(t, y, a, b, I):
    v, w = y
    dvdt = v - v**3 / 3 - w + I
    dwdt = (v + a - b * w) / 2
    return [dvdt, dwdt]

# Parámetros y condiciones iniciales
a = 0.7
b = 0.8
I = 0.5
y0 = [-0.6, 0.0]  # Condiciones iniciales

# Tiempo de integración
t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)

# Resolver las ecuaciones de FitzHugh-Nagumo
sol = solve_ivp(fitzhugh_nagumo, t_span, y0, args=(a, b, I), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Potencial de Membrana')
plt.title('Potencial de Membrana en el Modelo de FitzHugh-Nagumo')
plt.grid(True)
plt.show()
