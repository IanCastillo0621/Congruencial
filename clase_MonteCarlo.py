import random
import math

class montecarlo:
    def __init__(self, a,b,n,k,v):
        self.a = a
        self.b = b
        self.n = n
        self.k = k
        self.v = v
        self.resultado = [0]

    def CalcularSumatoriaUnificada(self):
        resultados_pre_escal = []
        resultados_pos_escal = []

        for i in range(self.n):
            numeros = []

            for j in range(self.v):
                val = random.random()
                numeros.append(val)


            asc = sorted(numeros)
            selec = asc[self.k - 1]

            resultados_pre_escal.append(selec)

            valorescalado =  self.a + (self.b - self.a) * selec

            resultados_pos_escal.append(valorescalado)

        self.resultado = resultados_pos_escal

    
    def calcular_estadisticas(self):
        promedio = sum(self.resultado) / self.n
        estadistico_final = self.resultado[-1]

        sum_cuadrados = sum((x - promedio) ** 2 for x in self.resultado)
        desviacion_estandar = math.sqrt(sum_cuadrados / self.n)

        return estadistico_final, promedio, desviacion_estandar







