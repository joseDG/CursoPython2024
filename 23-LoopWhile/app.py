monedas = 5

while monedas > 0:
  #print(f"tengo {monedas} monedas")
  monedas = monedas - 1

#ejercicio
respuesta = 's'
"""
while respuesta == 's':
  respuesta = input("Quires seguir ? (s/n)")
  pass
else:
  print("Gracias")
"""
#break
nombre = input("Tu nombre: ")

for letra in nombre:
  if letra == 'r':
    #break
    continue
  print(letra)