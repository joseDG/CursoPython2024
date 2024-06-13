class Pajaro:

  #metodo constructor
  def __init__(self, color, especie):
     self.color = color
     self.especie = especie


  def piar(self):
     print('Pio')


  def volar(self, metros):
     print(f"El pajaro ha volado {metros} metros")

#creacion de objetos
piolin = Pajaro('amarillo', 'canario')

#llamdno nuestros atributos
print(piolin.especie)

#llamar el metodo piar
piolin.piar()
#llamdno el metodo volar
piolin.volar(3)

