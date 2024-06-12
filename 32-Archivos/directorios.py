import os

#ruta = os.makedirs('C:\\Users\\Usuario iTC\\Documents\\CursoPython\\32-Archivos\\otra carpeta')
ruta = "C:\\Users\\Usuario iTC\\Documents\\CursoPython"
print(ruta)

elemento = os.path.split(ruta)
print(elemento)

os.rmdir('C:\\Users\\Usuario iTC\\Documents\\CursoPython\\32-Archivos\\otra carpeta')