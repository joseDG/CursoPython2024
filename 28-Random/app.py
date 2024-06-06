from random import *

#randint
aleatorio = randint(1, 50)
print(aleatorio)

#uniform
aleatorio = round(uniform(1,5),1)
print(aleatorio)

#random
print(random())

#choice
colores = ['azul','rojo','verde','negro']
aleatorio = choice(colores)
print(aleatorio)

#shuffle
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)