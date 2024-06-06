"""
Practica 3
Para acceder a un determinado puesto de trabajo, el candidato 
debe ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un 
candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

-"Cumples con los requisitos para postularte"
-"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
-"Para postularte, necesitas tener conocimientos de inglés"
-"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para
 plantear la estructura de control de flujo apropiada
  y verificar dichas condiciones. Evalúa a un candidato 
  que sabe inglés, pero no programa en Python.
"""

habla_ingles = True
sabe_python = False

if habla_ingles == True:
    if sabe_python == True:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python")
else:
    if sabe_python == True:
        print("Para postularte, necesitas tener conocimientos de inglés")
    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")