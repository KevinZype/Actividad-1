# Ejercicio 14

class Numero:
    """Clase que representa la entidad del número base."""
    def __init__(self, valor):
        self.valor = valor

class CalculadoraPotencias:
    """Clase encargada de ejecutar la lógica matemática."""
    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        self.cuadrado = self.numero.valor ** 2
        self.cubo = self.numero.valor ** 3

    def mostrar(self):
        print("\n--- RESULTADOS ---")
        print(f"Número base: {self.numero.valor}")
        print(f"Su cuadrado: {self.cuadrado}")
        print(f"Su cubo:     {self.cubo}")


# Ingreso y validación de datos
while True:
    try:
        entrada = int(input("Ingrese un número entero para calcular: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido (no letras ni decimales).")

mi_numero = Numero(entrada)

calculadora = CalculadoraPotencias(mi_numero)
calculadora.calcular()
calculadora.mostrar()