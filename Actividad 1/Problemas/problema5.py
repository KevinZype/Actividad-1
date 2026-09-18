# Ejercicio 17

import math

class Circulo:
    """Clase que representa la figura geométrica y su atributo principal."""
    def __init__(self, radio):
        self.radio = radio

class CalculadoraCirculo:
    """Clase encargada de ejecutar las operaciones matemáticas."""
    def __init__(self, circulo):
        self.circulo = circulo
        self.area = 0
        self.longitud = 0

    def calcular(self):
        self.area = int(math.pi * (self.circulo.radio ** 2))
        self.longitud = int(2 * math.pi * self.circulo.radio)

    def mostrar(self):
        print("\n--- RESULTADOS DEL CÍRCULO ---")
        print(f"Radio ingresado:               {self.circulo.radio}")
        print(f"Área del círculo:              {self.area}")
        print(f"Longitud de la circunferencia: {self.longitud}")


# Ingreso y validación de datos
while True:
    try:
        radio_input = int(input("Ingrese el radio del círculo: "))
        if radio_input > 0:
            break
        print("Error: El radio debe ser mayor a cero.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Ejecución del programa
mi_circulo = Circulo(radio_input)

calculadora = CalculadoraCirculo(mi_circulo)
calculadora.calcular()
calculadora.mostrar()