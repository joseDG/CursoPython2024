num1 = "hola"
num2 = "hola"

try:
  resultado = num1 / num2
except ZeroDivisionError:
  print("Error: Division por cero no permitida.")
except TypeError:
  print("Error: Ambos operandos deben ser numeros.")
finally:
  print("Operacion de division realizada")

#print(resultado)