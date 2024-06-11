import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


imagenes_juego = [piedra, papel, tijera]

eleccion_usuario = int(input("¿Que eliges? Escribe 0 para Piedra, 1 para Papel o 2 para Tijeras.\n"))


if eleccion_usuario >= 3 or eleccion_usuario < 0:
  print("Escribiste un numero no valido, Perdiste!")

else:
  print(imagenes_juego[eleccion_usuario])

  eleccion_computadora = random.randint(0, 2)
  print("Eleccion Computadora:")
  print(imagenes_juego[eleccion_computadora])

  if eleccion_usuario == 0 and eleccion_computadora == 2:
    print("Tu ganaste !")
  elif eleccion_computadora == 0 and eleccion_usuario == 2:
    print("Tu perdiste")
  elif eleccion_computadora > eleccion_usuario:
    print("Tu perdiste")
  elif eleccion_usuario > eleccion_computadora:
    print("Tu ganaste!")
  elif eleccion_computadora == eleccion_usuario:
    print("Es un empate")