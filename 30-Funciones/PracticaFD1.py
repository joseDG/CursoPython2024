"""
Practica 1

Crea una función (todos_positivos) que reciba una lista de números 
como parámetro, y devuelva True si todos los valores de una lista 
son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.
"""

lista_numeros = [1,-50,502,-5000,755,600,33,61]

def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

print(todos_positivos(lista_numeros))