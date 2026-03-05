from math import sin, cos, pi
import matplotlib.pyplot as plt

# Aproximación por diferencia hacia adelante
def diff_point(x0, f, h):
    return (f(x0 + h) - f(x0)) / h

def main():
    f  = lambda x: sin(x)
    df = lambda x: cos(x)

    x0 = pi/6  # punto donde derivamos
    hs = [1e-1, 5e-1, 1e-2, 1e-3, 1e-4]

    true_value = df(x0)

    approx = []
    error  = []

    for h in hs:
        d = diff_point(x0, f, h)
        approx.append(d)
        error.append(abs(true_value - d))

    # Mostrar resultados
    print("h        Aproximación        Error")
    for h, a, e in zip(hs, approx, error):
        print(f"{h:.1e}   {a:.10f}     {e:.10e}")

    # Gráfica del error
    plt.figure()
    plt.loglog(hs, error)   # escala log-log
    plt.xlabel("h")
    plt.ylabel("Error absoluto")
    plt.title("Error de la derivada numérica de sin(t) en t = pi/6")
    plt.show()

if __name__ == "__main__":
    main()