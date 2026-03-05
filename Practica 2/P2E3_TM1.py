import matplotlib.pyplot as plt

def fde(r, b, x0, N=20):
    x = [x0]
    for n in range(N-1):
        x.append(r*x[n] + b)
    return x

casos = [
    (0.5, 2, 1),
    (1,   1, 1),
    (2,   0, 1),
    (2,   2, 1)
]

plt.figure(figsize=(10,6))

for r, b, x0 in casos:
    x = fde(r, b, x0)
    plt.plot(x, 'o-', label=rf"$r={r},\ b={b},\ x_0={x0}$")

plt.xlabel("n")
plt.ylabel("$x_n$")
plt.title("Ecuación en diferencias: $x_{n+1}=rx_n+b$")
plt.legend()
plt.grid(True)
plt.show()
#Cuando $r=0.5, b=2, x_0=1$ La sucesión converge a un punto fijo. $x=\frac{b}{1−r} = \frac{2}{0.5}=4$ Por lo que es estable.

#Cuando $r=1=b=x_0$ obtenemos la ecuacion $x_{n}= n+1$ , ie, tenemos un crecimiento lienal

#Cuando $r=2 , b=0, x_0=1$  se tiene una solución de la forma $x_n= 2^n$ que es un crecimento exponencial y no estable

#El siguiente caso es analogo al anterior pero crece más rápido.

