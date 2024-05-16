import sympy as sp
import numpy as np

# Definir variables simbólicas
a, b = sp.symbols('a b')

# Definir una expresión simbólica simple
expr = a**2 + sp.sqrt(b)

# Convertir la expresión simbólica a una función numérica
num_func = sp.lambdify((a, b), expr, modules=['numpy'])

# Evaluar la función numérica para valores específicos
a_val = 3
b_val = 4
result = num_func(a_val, b_val)
print(f"num_func({a_val}, {b_val}) = {result}")

# Evaluar la función numérica para arrays de valores
a_vals = np.linspace(1, 10, 10)
b_vals = np.linspace(1, 10, 10)
results = num_func(a_vals, b_vals)
print(f"num_func(a_vals, b_vals) = {results}")
