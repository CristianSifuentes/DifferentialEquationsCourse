import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos y de la simulación
L = 10  # Longitud de la barra
T_max = 100  # Temperatura máxima permitida
D = 1.0  # Difusividad térmica
Nx = 100  # Número de puntos de malla espacial
Nt = 1000  # Número de pasos de tiempo
dt = 0.01  # Tamaño de paso de tiempo
dx = L / (Nx - 1)  # Tamaño del paso espacial

# Condiciones iniciales y de contorno
T_ini = np.zeros(Nx)  # Temperatura inicial en toda la barra
T_ini[0] = 100  # Temperatura inicial en el extremo izquierdo
T_ini[-1] = 0  # Temperatura inicial en el extremo derecho

# Crear una matriz para almacenar la temperatura en cada punto de la malla en cada paso de tiempo
T = np.zeros((Nt, Nx))

# Asignar condiciones iniciales
T[0, :] = T_ini

# Iterar en el tiempo y espacio para resolver la ecuación de calor
for n in range(1, Nt):
    for i in range(1, Nx - 1):
        T[n, i] = T[n-1, i] + dt * (D * (T[n-1, i-1] - 2*T[n-1, i] + T[n-1, i+1]) / dx**2)

# Crear una malla espacial
x = np.linspace(0, L, Nx)

# Visualización de la solución
plt.figure(figsize=(10, 6))
for n in range(0, Nt, Nt // 10):
    plt.plot(x, T[n, :], label=f'Tiempo {n * dt:.2f}')
plt.xlabel('Posición')
plt.ylabel('Temperatura')
plt.title('Propagación del Pulso de Calor en una Barra Metálica')
plt.legend()
plt.grid(True)
plt.show()
