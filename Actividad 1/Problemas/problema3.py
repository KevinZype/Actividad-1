# Ejercicio 12

class Empleado:
    """Clase que representa únicamente los datos laborales del trabajador."""
    def __init__(self, horas, valor):
        self.horas_trabajadas = horas
        self.valor_hora = valor

class LiquidacionNomina:
    """Clase encargada de procesar los cálculos matemáticos de la nómina."""
    def __init__(self, empleado, porcentaje_ret):
        self.empleado = empleado
        self.porcentaje_ret = porcentaje_ret
        
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular(self):
        self.salario_bruto = int(self.empleado.horas_trabajadas * self.empleado.valor_hora)
        self.retencion = int(self.salario_bruto * (self.porcentaje_ret / 100))
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar(self):
        print("\n--- RESULTADOS DE NÓMINA ---")
        print(f"Salario Bruto: ${self.salario_bruto}")
        print(f"Retención en la fuente: ${self.retencion}")
        print(f"Salario Neto: ${self.salario_neto}")


# 1. Ingreso y validación de datos
print("Ingrese los datos del trabajador:")

while True:
    horas = int(input("Horas trabajadas en la semana: "))
    if horas > 0:
        break
    print("Error: Las horas deben ser mayores a cero.")

while True:
    valor = int(input("Valor por hora: "))
    if valor > 0:
        break
    print("Error: El valor por hora debe ser mayor a cero.")

while True:
    porcentaje = float(input("Porcentaje de retención: "))
    if porcentaje >= 0:
        break
    print("Error: El porcentaje no puede ser negativo.")

# 2. Ejecución con múltiples clases
trabajador = Empleado(horas, valor)

liquidacion = LiquidacionNomina(trabajador, porcentaje)
liquidacion.calcular()
liquidacion.mostrar()