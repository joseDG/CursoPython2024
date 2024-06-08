#funcion que sume los numeros
def sumar_todos(*args):
  suma = 0
  for n in args:
    suma += n
  return suma

print(sumar_todos(1,2,3)) # resutlado=6
print(sumar_todos(10,20,30,50)) #resultado = 110
