#archivo = open('prueba2.txt', 'w')
#archivo.write('hola\n')
#archivo.write('mundo')

#modificar archivo
archivo = open('prueba2.txt', 'a') 

lista = ['hola', 'mundo','estoy']

for l in lista:
  archivo.writelines(l + '\n')

archivo.write('Bienvenidos')

archivo.close()
