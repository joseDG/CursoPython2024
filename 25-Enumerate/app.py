lista = ['a', 'b', 'c']
indice = 0

for item in lista:
  print(indice, item)
  #operadores de asignacion
  indice += 1

print("\n")
#con enumerate
lista = ['a', 'b', 'c']

for i, item in enumerate(lista):
  print(i, item)

#combinacion de enumerate con range
print("\n")
for i, item in enumerate(range(50,55)):
  print(f"{i} - {item}")

#crear una lista de tuplas
print("\n")
lista = ['a', 'b', 'c']

mis_tuplas = list(enumerate(lista))
print(mis_tuplas)
print(mis_tuplas[1][1])
