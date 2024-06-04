#Solitar Informacion al cliente
input("Dime tu nombre: ")
input("Dime tu apellido: ")

""""
Creacion de Inputs y 
usando el print 
"""

print(input("Dime tu nombre:"))
print(input("Nombres Completos: " + input("Dime tu nombre: ") + " " + input("Dime tu apellido: ")))

#Forma correcta
print("Nombres Completos: " + (input("Dime tu nombre: ")) + " " + (input("Dime tu apellido: ")))
