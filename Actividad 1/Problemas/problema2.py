# Ejercicio 5

class PruebaEscritorio:
    def __init__(self, x, y):
        self.SUMA = 0
        self.X = x
        self.Y = y

    def ejecutar(self):
        self.SUMA = self.SUMA + self.X
        self.X = self.X + (self.Y ** 2)
        self.SUMA = self.SUMA + (self.X / self.Y)

    def mostrar(self):
        print(f"EL VALOR DE LA SUMA ES: {self.SUMA}")

# Ingreso de datos
x = int(input("Ingrese el valor de X: "))

while True:
    y = int(input("Ingrese el valor de Y: "))
    if y != 0:
        break
    print("Error: Y no puede ser cero porque causa una división por cero.")

# Ejecución
ejercicio = PruebaEscritorio(x, y)
ejercicio.ejecutar()
ejercicio.mostrar()