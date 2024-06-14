class CD:

  def __init__(self, autor, album, canciones):
    self.autor = autor
    self.album = album 
    self.caciones = canciones

  def __str__(self):
    return f"Album {self.album} de {self.autor}"
  
  def __len__(self):
    return self.caciones
  
  def __del__(self):
    print("Se ha eliminado el cd")


mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
