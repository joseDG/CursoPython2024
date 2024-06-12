from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\Usuario iTC\\Documents\\CursoPython\\32-Archivos\\otra carpeta')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

if not carpeta.exists():
  print("Este archivo no existe")
else:
  print("Genial, existe")