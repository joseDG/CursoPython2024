class Animal:

  def __init__(self, edad, color):
    self.edad = edad
    self.color = color

  
  def nacer(self):
    print("Este animal anacido")

  def hablar(self):
    print("Este animal emite un sonido")


class Pajaro(Animal):
  def __init__(self, edad, color, altura_vuelo):
    super().__init__(edad, color)
    self.altura_vuelo = altura_vuelo

  def hablar(self):
    return super().hablar()
  
  def volar(self, metros):
    print(f"El pajaro vuela {metros} metros")

  number = 5

piolin = Pajaro(10, "Amarillo", 3)
piolin.nacer()
piolin.hablar()




