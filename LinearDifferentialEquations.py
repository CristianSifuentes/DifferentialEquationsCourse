import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Importación de bibliotecas:
# numpy se usa para operaciones numéricas y creación de arreglos.
# matplotlib.pyplot se usa para la creación de gráficos.
# sympy se usa para operaciones simbólicas, como la solución de ecuaciones diferenciales.


# Definir las variables y la función
x, C = sp.symbols('x C')
y = sp.Function('y')(x)


# Definición de variables simbólicas:
# x y C son variables simbólicas.
# y es una función simbólica de x.

# Una variable simbólica es un objeto en python que representa una incógnita que puede tomar cualquier valor. 
# Por tanto, una operación que involucra una o más variables simbólicas no devuelve un valor numérico, 
# sino una expresión simbólica que involucra números, operaciones, funciones y variables simbólicas.


# Definir la ecuación diferencial
ode = sp.Eq(y.diff(x) + 3*y, 6*x)

# Definición de la ecuación diferencial:
# y.diff(x) representa la derivada de y con respecto a x.
# sp.Eq define la ecuación diferencial: 
# 𝑑𝑦/𝑑𝑥 + 3𝑦 = 6𝑥 dx/dy


# Resolver la ecuación diferencial
solution = sp.dsolve(ode, y)
y_sol = solution.rhs

# Solución de la ecuación diferencial:
# sp.dsolve resuelve la ecuación diferencial.
# solution.rhs obtiene la parte derecha de la solución general.


# Mostrar la solución general
print(f"Solución general: y = {y_sol}")

# Impresión de la solución general:
# Se imprime la solución general de la ecuación diferencial.

# Convertir la solución simbólica a una función numérica
y_func = sp.lambdify((x, C), y_sol, modules=['numpy'])

# sp.lambdify convierte la solución simbólica a una función numérica que puede ser evaluada con numpy.


# Definir un rango de valores para x
x_vals = np.linspace(0, 5, 400)

# np.linspace crea un arreglo de 400 valores equidistantes entre 0 y 5.


# Elegir un valor arbitrario para la constante de integración
C_val = 1  # Puedes cambiar este valor para ver cómo cambia la solución
# C_val se define como 1. Este valor puede cambiarse para ver cómo afecta la solución.


# Calcular los valores de y para los valores de x dados
y_vals = y_func(x_vals, C_val)
# y_func se evalúa con los valores de x y la constante C_val para obtener los valores correspondientes de y.


# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'C = {C_val}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la ecuación diferencial $\\frac{dy}{dx} + 3y = 6x$')
plt.legend()
plt.grid(True)
plt.show()

# Se crea una figura de tamaño 10x6.
# plt.plot grafica x_vals contra y_vals.
# Se añaden etiquetas para los ejes x e y, y un título para la gráfica.
# plt.legend añade una leyenda mostrando el valor de C.
# plt.grid añade una cuadrícula a la gráfica.
# plt.show muestra la gráfica.

# En resumen, este código resuelve la ecuación diferencial 

# 𝑑𝑦/𝑑𝑥 + 3𝑦 = 6𝑥 dx/dy
# ​
# usando SymPy, convierte la solución simbólica en una función numérica con NumPy, 
# y finalmente grafica la solución para un rango de valores de x utilizando Matplotlib.
