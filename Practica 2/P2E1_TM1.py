import matplotlib.pyplot as plt

# Función FDE
def fde(P0, k, n):
    P = [P0]
    for i in range(n):
        P.append(k * P[i])
    return P

# Parámetros
P0 = 2
n = 100
ks = [2, 1, 0.5, -0.5, -2]

# Crear figura con subplots
fig, axes = plt.subplots(5, 1, figsize=(8, 12))

for i, k in enumerate(ks):
    P = fde(P0, k, n)
    axes[i].plot(P)
    axes[i].set_title(f"k = {k}")
    axes[i].set_xlabel("n")
    axes[i].set_ylabel("P_n")
    axes[i].grid(True)
plt.tight_layout()
plt.show()

#Notenos que tenemos la ecuación  Pn+1=kPn, P0=2  al iterar tenemos la solución explicita  Pn=P0k2=2kn  por lo que el comportamineto del sistema depende de  k .
#Cuando  k=2  Se observa crecimiento exponencial. La sucesión diverge a infinito, por lo que el sistema es inestable.
#Cuando  k=1  a sucesión permanece constante  Pn=2  El sistema es estable en equilibrio neutro.

#Cuando  k=0.5  La sucesión decrece exponencialmente y tiende a cero:

#Cuando  k=−0.5  La sucesión oscila en signo y se amortigua hacia cero.

#Cuando  k=−2  La sucesión oscila y crece sin límite en magnitud.

