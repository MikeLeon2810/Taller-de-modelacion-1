# ============================================================
# MODELO SIR EN ECUACIONES EN DIFERENCIAS
# ============================================================

# El modelo SIR divide la población total N en tres grupos:
#
# S(n) = número de susceptibles en el tiempo n
# I(n) = número de infectados en el tiempo n
# R(n) = número de removidos (recuperados o fallecidos) en el tiempo n
#
# Se cumple siempre:
#
# S(n) + I(n) + R(n) = N   (población total constante)
#
# ------------------------------------------------------------
# PARÁMETROS DEL MODELO
# ------------------------------------------------------------
#
# alfa  = tasa de contacto efectivo (tasa de contagio)
# gamma = tasa de recuperación
#
# ------------------------------------------------------------
# SISTEMA EN DIFERENCIAS
# ------------------------------------------------------------
#
# S(n+1) = S(n) - alfa * S(n)*I(n) / N
#
# I(n+1) = I(n) + alfa * S(n)*I(n) / N - gamma*I(n)
#
# R(n+1) = R(n) + gamma*I(n)
#
# Interpretación:
#
# - alfa*S(n)*I(n)/N  representa los nuevos contagios.
# - gamma*I(n)        representa los infectados que se recuperan
#----------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def SIR(S0, I0, R0, alfa, gamma, n, Plot=True):
    N = S0 + I0 + R0

    S = [S0]
    I = [I0]
    R = [R0]

    for k in range(n - 1):
        Sn = S[-1]
        In = I[-1]
        Rn = R[-1]

        S_next = Sn - alfa * Sn * In / N
        I_next = In + alfa * Sn * In / N - gamma * In
        R_next = Rn + gamma * In

        S.append(S_next)
        I.append(I_next)
        R.append(R_next)

    # -------------------------
    # IMPRESIÓN TIPO TABLA
    # -------------------------
    print("\nTabla de valores del modelo SIR\n")
    print("n\tS(n)\t\tI(n)\t\tR(n)")
    print("-" * 60)

    for t in range(n):
        print(f"{t}\t{S[t]:.2f}\t{I[t]:.2f}\t{R[t]:.2f}")

    # -------------------------
    # GRÁFICA
    # -------------------------
    if Plot:
        plt.plot(range(n), S, label='S(n)')
        plt.plot(range(n), I, label='I(n)')
        plt.plot(range(n), R, label='R(n)')
        plt.legend()
        plt.xlabel('Tiempo (n)')
        plt.ylabel('Población')
        plt.title('Modelo SIR')
        plt.grid(True)
        plt.show()

    return (S, I, R)

if __name__ == '__main__':
 S0 = 1000000
 I0 = 127
 R0 = 0
 alfa = 1
 gamma = 0.6
 n = 150

 S, I, R = SIR(S0, I0, R0, alfa, gamma, n)