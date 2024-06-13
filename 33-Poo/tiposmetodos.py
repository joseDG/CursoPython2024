class Pajaro:

  alas = True

  #metodo constructor
  def __init__(self, color, especie):
     self.color = color
     self.especie = especie


  def piar(self):
     print('Pio')


  def volar(self, metros):
     print(f"El pajaro ha volado {metros} metros")

  #metodo de instancia
  def pintar_negro(self):
     self.color = "negro"
     print(f"Ahora el pajaro es {self.color}")

  #metodo de clase
  @classmethod
  def poner_huevos(cls, cantidad):
     print(f"Puso {cantidad} huevos")
     cls.alas = False
     print(Pajaro.alas)

  #metodos estaticos
  @staticmethod
  def mirar():
     print("El pajaro mira")


#creacion de objetos
piolin = Pajaro('amarillo', 'canario')
print(piolin.color)
print(piolin.poner_huevos(5))





