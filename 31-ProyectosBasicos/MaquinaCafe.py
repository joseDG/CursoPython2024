MENU = {
  "expresso":{
    "ingredientes":{
      "agua": 50,
      "cafe": 18,
    },
    "costo": 1.50,
  },
  
  "latte" : {
    "ingredientes":{
      "agua": 200,
      "leche": 150,
      "cafe": 24,
    },
    "costo": 2.50,
  },

  "cappuccino":{
    "ingredientes":{
      "agua": 250,
      "leche": 100,
      "cafe": 24,
    },
    "costo": 3.00,
  }
}

ganancia = 0
recursos = {
  "agua": 300,
  "leche": 200,
  "cafe": 100,
}

def es_recurso_suficiente(orden_ingredientes):
  """Devuelve verdadero cuando se puede realizar el pedido, False si los ingredientes son insuficientes"""
  for item in orden_ingredientes:
    if orden_ingredientes[item] > recursos[item]:
      print(f"Lo siento, no hay suficiente {item} .")
      return False
  return True


def proceso_monedas():
  """Devuelve el total calculado a partir de las monedas insertadas."""
  print("Por favor inserte monedas.")
  total = int(input("¿Cuantas monedas de venticinco centavos?: ")) * 0.25
  total += int(input("¿Cuantas monedas de diez centavos?: ")) *0.1
  total += int(input("¿Cuantas monedas de cinco centavos?: ")) *0.05
  total += int(input("¿Cuantas monedas de centavo?: ")) *0.01
  return total

def es_transaccion_exitosa(dinero_recibio, costo_bebida):
  """Devuelve V cuando se acepta el pago, False si el dinero es insuficiente."""
  if dinero_recibio >= costo_bebida:
    cambio = round(dinero_recibio - costo_bebida, 2)
    print(f"Aqui esta ${cambio} el cambio")
    global ganancia
    ganancia += costo_bebida
    return True
  else:
    print("Lo siento, no es suficiente dinero. Dinero reembolsado.")
    return False
  
def hacer_cafe(nombre_bebida, orden_ingredientes):
  """Deducir los ingredientes neceserios de los recursos."""
  for item in orden_ingredientes:
    recursos[item] -= orden_ingredientes[item]
  print(f"Aqui esta tu {nombre_bebida} ☕. ¡Disfrutar!")  


esta_encendida = True

while esta_encendida:
  eleccion = input("¿Que te gustaria? (expresso/latte/cappuccino): ")
  if eleccion == "off":
    esta_encendida = False
  elif eleccion == "reporte":
    print(f"Agua: {recursos['agua']}ml")
    print(f"Leche: {recursos['leche']}ml")
    print(f"Cafe: {recursos['agua']}g")
    print(f"Dinero: ${ganancia}")
  else:
    tomar = MENU[eleccion]
    if es_recurso_suficiente(tomar["ingredientes"]):
      pagar = proceso_monedas()
      if es_transaccion_exitosa(pagar, tomar["costo"]):
        hacer_cafe(eleccion, tomar["ingredientes"])


