import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones de Hodgkin-Huxley
def hodgkin_huxley(t, y, I_ext):
    V, m, h, n = y
    C_m = 1.0  # Capacitancia de la membrana (uF/cm^2)
    g_Na = 120.0  # Conductancia máxima de sodio (mS/cm^2)
    g_K = 36.0  # Conductancia máxima de potasio (mS/cm^2)
    g_L = 0.3  # Conductancia máxima de fuga (mS/cm^2)
    E_Na = 50.0  # Potencial de equilibrio de sodio (mV)
    E_K = -77.0  # Potencial de equilibrio de potasio (mV)
    E_L = -54.387  # Potencial de equilibrio de fuga (mV)

    alpha_m = (2.5 - 0.1 * V) / (np.exp(2.5 - 0.1 * V) - 1)
    beta_m = 4 * np.exp(-V / 18)
    alpha_h = 0.07 * np.exp(-V / 20)
    beta_h = 1 / (np.exp(3 - 0.1 * V) + 1)
    alpha_n = (0.1 - 0.01 * V) / (np.exp(1 - 0.1 * V) - 1)
    beta_n = 0.125 * np.exp(-V / 80)

    I_Na = g_Na * m**3 * h * (V - E_Na)
    I_K = g_K * n**4 * (V - E_K)
    I_L = g_L * (V - E_L)
    dVdt = (I_ext - I_Na - I_K - I_L) / C_m
    dmdt = alpha_m * (1 - m) - beta_m * m
    dhdt = alpha_h * (1 - h) - beta_h * h
    dndt = alpha_n * (1 - n) - beta_n * n
    return [dVdt, dmdt, dhdt, dndt]

# Parámetros y condiciones iniciales
I_ext = 10.0  # Corriente externa aplicada (uA/cm^2)
y0 = [-65, 0.05, 0.6, 0.3]  # Potencial de membrana inicial y valores iniciales de compuertas

# Tiempo de integración
t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)

# Resolver las ecuaciones de Hodgkin-Huxley
sol = solve_ivp(hodgkin_huxley, t_span, y0, args=(I_ext,), t_eval=t_eval)

# Visualizar la solución
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo (ms)')
plt.ylabel('Potencial de Membrana (mV)')
plt.title('Potencial de Membrana de una Neurona (Hodgkin-Huxley)')
plt.grid(True)
plt.show()
