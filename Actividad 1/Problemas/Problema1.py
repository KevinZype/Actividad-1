# Ejercicio 4

class EdadesFamilia:
    def __init__(self, edjuan):
        self.EDJUAN = edjuan
        self.EDALBER = 0
        self.EDANA = 0
        self.EDMAMA = 0

    def calcular(self):
        self.EDALBER = int((2/3) * self.EDJUAN)
        self.EDANA = int((4/3) * self.EDJUAN)
        self.EDMAMA = self.EDALBER + self.EDJUAN + self.EDANA

    def mostrar(self):
        print(f"Edad de Juan: {self.EDJUAN} años")
        print(f"Edad de Alberto: {self.EDALBER} años")
        print(f"Edad de Ana: {self.EDANA} años")
        print(f"Edad de la mamá: {self.EDMAMA} años")


# Ingreso y validación de datos
while True:
    edjuan = int(input("Ingrese la edad de Juan: "))
    if edjuan > 0:
        break
    print("Error: La edad debe ser un número mayor a cero.")

# Ejecución
ejercicio = EdadesFamilia(edjuan)
ejercicio.calcular()
ejercicio.mostrar()