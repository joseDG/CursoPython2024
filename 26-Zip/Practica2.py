"""
Practica 2

Crea un objeto zip formado a partir de listas, de un 
conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
"""

marcas = ['Nike', 'Adidas', 'Rebook']
producto = ['Zapatillas', 'Camiseta', 'Medias']

mi_zip = list(zip(marcas, producto))

print(mi_zip)