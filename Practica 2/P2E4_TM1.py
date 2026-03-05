#La solución excacta (por medio de variables separables) es $-3x^2+ 3x+2$ minetras que la de diferencias finitas es
#$y_{n+1} =y_n +\Delta x(-6x_n+3)$ , donde $x_{n+1}=\Delta x +x_n $

import numpy as np
import matplotlib.pyplot as plt

# Solución exacta
def y_exact(x):
    return -3*x**2 + 3*x + 2

# Euler
def euler(dx, N):
    x = np.zeros(N)
    y = np.zeros(N)
    y[0] = 2
    for n in range(N-1):
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dx * (-6*x[n] + 3)
    return x, y

# Parámetros
deltas = [0.5, 5, 20]
N = 7
x_cont = np.linspace(0, 50, 300)

plt.figure(figsize=(10,6))

# Solución exacta
plt.plot(x_cont, y_exact(x_cont), 'k',
         label=r"$y(x) = -3x^2 + 3x + 2$")

# Euler para cada delta
for dx in deltas:
    x, y = euler(dx, N)
    plt.plot(x, y, 'o-',
             label=rf"$y_{{n+1}}=y_n+\Delta x(-6x_n+3),\ \Delta x={dx}$")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparación solución exacta vs método de Euler")
plt.legend()
plt.grid(True)
plt.show()