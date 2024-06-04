mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

#tamano de la lista
print(len(mi_lista))

#unir listas
mi_lista1 = ['a', 'b', 'c']
mi_lista2 = ['s', 'd', 'f']
print(mi_lista1 + mi_lista2)

#slice in listas
resultado = mi_lista[0:]
print(resultado)

#sobre escribir valores en una lista
mi_lista4 = ['z','f','g']
mi_lista4[2] = "alfa"
print(mi_lista4)

#metodo de agregar
mi_lista4.append('h')
print(mi_lista4)

#metodo para eliminar
mi_lista4.pop(0)
print(mi_lista4)

#ordenar listas
mi_lista6 = [1, 10, 2, 3, 13, 4, 15, 5, 35, 86, 99]
mi_lista6.sort()
print(mi_lista6)

mi_lista5 = ["a","x","n","e","y"]
mi_lista5.sort()
print(mi_lista5)