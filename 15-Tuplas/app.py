#son inmutables -> no se pueden editar

mi_tupla = (1,2,(10,20),4)
print(type(mi_tupla))
print(mi_tupla[2][0])

#conversion
mi_tupla = list(mi_tupla)
print(type(mi_tupla))

#asignar a diferentes variables
t = (1,2,3)
x,y,z = t 
print(x,y,z)

#aplicando metodos en tuplas count() - index()
t = (1,2,3,1)
print(t.count(1))
print(t.index(3))