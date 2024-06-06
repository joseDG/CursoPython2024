nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,45,23]
#agregar ciudades
ciudades = ['Lima', 'Madrid', 'Mexico', 'Ecuador']

combinados = list(zip(nombre, edades, ciudades))
#print(combinados)

#crear un loop
for nombre, edad, ciudad in combinados:
  print(f"{nombre} tiene {edad} years y vive en {ciudad}")