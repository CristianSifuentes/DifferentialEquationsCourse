import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# import sympy as sp
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D



print('matplotlib: {}'.format(matplotlib.__version__))

# Definir variables simbólicas
a, b = sp.symbols('a b')

# Definir una expresión simbólica simple
expr = a**2 + sp.sqrt(b)

# Convertir la expresión simbólica a una función numérica
num_func = sp.lambdify((a, b), expr, modules=['numpy'])

# Definir rangos de valores para a y b
a_vals = np.linspace(1, 10, 100)
b_vals = np.linspace(1, 10, 100)

# Crear una cuadrícula de valores de a y b para evaluar la función
A, B = np.meshgrid(a_vals, b_vals)
Z = num_func(A, B)

# Crear la gráfica de superficie
fig = plt.figure(figsize=(10, 6))
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(A, B, Z, cmap='viridis')

# Añadir etiquetas y título
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('f(a, b)')
ax.set_title('Gráfica de la función $f(a, b) = a^2 + \sqrt{b}$')

# Añadir barra de color
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Mostrar la gráfica
plt.show()


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 
# fig = plt.figure()

# ax = Axes3D(fig) #<-- Note the difference from your original code...

# X, Y, Z = axes3d.get_test_data(0.05)
# cset = ax.contour(X, Y, Z, 16, extend3d=True)
# ax.clabel(cset, fontsize=9, inline=1)
# plt.show()
