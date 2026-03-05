import matplotlib.pyplot as plt

def SIR(S0, I0, R0, alfa, beta, n, Plot=True, titulo="Modelo SIR"):
    """
    Simula el modelo SIR discreto durante n-1 pasos, devolviendo listas
    de longitud n (desde tiempo 0 hasta n-1).
    """
    # Población total constante
    N = S0 + I0 + R0

    # Inicializar listas con las condiciones iniciales
    S = [S0]
    I = [I0]
    R = [R0]

    # Iterar para obtener los siguientes n-1 valores
    for k in range(n - 1):
        s_actual = S[-1]
        i_actual = I[-1]
        r_actual = R[-1]

        # Nuevos infectados (ley de masas)
        nuevos_infectados = alfa * s_actual * i_actual / N
        nuevos_recuperados = beta * i_actual

        s_siguiente = s_actual - nuevos_infectados
        i_siguiente = i_actual + nuevos_infectados - nuevos_recuperados
        r_siguiente = r_actual + nuevos_recuperados

        S.append(s_siguiente)
        I.append(i_siguiente)
        R.append(r_siguiente)

    # Graficar si se solicita
    if Plot:
        plt.plot(range(0, n, 1), S, 'm', label='S(n)')
        plt.plot(range(0, n, 1), I, 'b', label='I(n)')
        plt.plot(range(0, n, 1), R, 'g', label='R(n)')
        plt.legend()
        plt.xlabel('Tiempo (n)')
        plt.ylabel('Población')
        plt.title(titulo)  # Usar el título personalizado
        plt.grid(True)
        plt.show()

    return (S, I, R)

# Caso 1
print("Caso 1:")
S1, I1, R1 = SIR(100000, 200000, 0, 0.7, 0.5, 50, Plot=True, titulo="Modelo SIR - Caso 1")

# Caso 2
print("Caso 2:")
S2, I2, R2 = SIR(200000, 100000, 0, 0.75, 0.5, 50, Plot=True, titulo="Modelo SIR - Caso 2")
#En los casos 1 y 2 se redujo a n=50 porque usando el valor pedido en la práctica se volvia ilegible la grafica correspondiente.
#Esto no afecta en nada ya que tanto en la n origina como en la modifica se aprecia que Sn e In se vuelven constantes depues de un tiempo t.
# Caso 3
print("Caso 3:")
S3, I3, R3 = SIR(1000000, 10, 0, 0.75, 0.5, 100, Plot=True, titulo="Modelo SIR - Caso 3")