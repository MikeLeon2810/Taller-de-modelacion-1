import matplotlib.pyplot as plt

def SIR(S0, I0, R0, alfa, beta, n, Plot = True):
    #obtenemos la poblacion total
    N = S0 + I0 + R0
    #listas de los tres tipos de personas en nuestra poblacion
    S = [S0]
    I = [I0]
    R = [R0]
    #agregamos uno por uno los n valores que nos piden, utilizando las formulas que nos proporcionan
    for _ in range(n):
        #formulas
        siguiente_S = S[-1] - (alfa*S[-1]*I[-1])/N
        siguiente_I = I[-1] + ((alfa*S[-1]*I[-1])/N) - beta*I[-1]
        #agregamos
        S.append(siguiente_S)
        I.append(siguiente_I)
        R.append(N-I[-1]-S[-1])
    #graficamos
    if Plot:
        plt.plot(range(0,n+1,1), S, 'm', label = 'S(n)')
        plt.plot(range(0,n+1,1), I, 'b', label = 'I(n)')
        plt.plot(range(0,n+1,1), R, 'g', label = 'R(n)')
        plt.legend()
        plt.xlabel('Tiempo (n)')
        plt.ylabel('Población')
        plt.title('Modelo SIR')
        plt.grid(True)
        plt.show()


#Ejercicio 3.

S0 = [1_000_000, 200_000, 1_000_000]
I0 = [200_000, 100_000, 10]
alfa = [0.7, 0.75, 0.75]
beta = [0.5, 0.5, 0.5] #Creamos listas con los valores de cada variable
N = []
for i in range(3):
  Ni = S0[i] + I0[i] #Calculamos las respectivas N
  N.append(Ni)
R0 = []
for i in range(3):
  Ri = (alfa[i]*S0[i])/(beta[i]*N[i]) #Calculamos los respectivos R0
  R0.append(Ri)
print(f"Valores de R0 (caso 1,2,3): {R0}")
for i in range(3):
  SIR(S0[i], I0[i], 0, alfa[i], beta[i], 150)
  print(f"R0 = {R0[i]}")
