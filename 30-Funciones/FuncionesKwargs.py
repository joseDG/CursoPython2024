#cantidad de atributos
def cantidad_atributos(**kwargs):
  cantida = 0
  for i in  kwargs.items():
    cantida += 1
  return cantida

#print(cantidad_atributos(a=1, b=2, c=20))


def imprimir_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:{value}")

imprimir_kwargs(nombre = "Jose", edad = 30 , ciudad= "Loja")

def configurar_opciones(obligatorio, **kwargs):
  opciones = {
    'opcion1' : 'valor por defecto 1',
    'opcion2' : 'valor por defecto 2',
  }
  opciones.update(kwargs)
  print(f"Obligatorio: {obligatorio}")
  for key , value in opciones.items():
    print(f"{key} : {value}")

configurar_opciones('necesario', opcion1 = "nuevo valor 1", opcion2 = "nuevo valor 2")