#La ecuación lógistica  $\frac{dP}{dt} = rp\left(1- \frac{P}{k} \right)$ se ve como la siguiente ecuación en diferencias finitas $$P_{n+1} = P_n +rP_n  \left(1- \frac{P_n}{k}\right)$$
#(El desarrollo se hizo en clase)
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.5
k = 1000
N = 40  # número de iteraciones (puedes aumentar si quieres)

# Condiciones iniciales
P0_values = [5, 1000, 1500]

# Función logística discreta
def logistic_map(P0, r, k, N):
    P = np.zeros(N)
    P[0] = P0
    for n in range(N-1):
        P[n+1] = P[n] + r * P[n] * (1 - P[n]/k)
    return P

# Gráfica
plt.figure(figsize=(10,6))

for P0 in P0_values:
    P = logistic_map(P0, r, k, N)
    plt.plot(P, label=f"P0 = {P0}")

# Etiquetas y leyenda
plt.xlabel("n (tiempo discreto)")
plt.ylabel("P_n (población)")
plt.title("Modelo logístico discreto para diferentes condiciones iniciales")
plt.legend()
plt.grid(True)

plt.show()
#Cuando $P_0 =5$ La población crece rápidamente al inicio y luego se desacelera.
#Se aproxima a $k=1000$ sin sobrepasarlo.

#Cunado $P_0= 1000$ La población permanece constante en 1000

#Cuando $P_0= 1500$ La población disminuye hasta acercarse a 1000.