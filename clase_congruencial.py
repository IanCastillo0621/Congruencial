
class congruencial:
    def __init__(self, semilla, a, c, m):
        self.semilla = semilla 
        self.a = a
        self.c = c
        self.m = m
        self.x = semilla  

    def generar_congruencial(self):
        secuencia = []
        while True:
            self.x = (self.a * self.x + self.c) % self.m
            if self.x in secuencia:
                break
            
            secuencia.append(self.x)
        return secuencia

