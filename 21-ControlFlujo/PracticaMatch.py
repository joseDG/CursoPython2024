"""
Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación, división).
"""

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))

operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").lower()

match operacion:
  case 'suma':
    resultado = numero1 + numero2
  case 'resta':
    resultado = numero1 - numero2
  case 'multiplicacion':
    resultado = numero1 * numero2
  case 'division':
    resultado = numero1 / numero2
  case _:
    resultado = "Operacion Invalida"

print(f"Resultado: {resultado}")