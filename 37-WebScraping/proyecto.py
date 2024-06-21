import requests
import bs4 # type: ignore

#crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista de titulos con 4 0 5 estrellas
titulos_rating_alto = []

#iterar entre paginas
for pagina in range(1, 51):
  #crear soup en cada pagina
  url_pagina = url_base.format(pagina)
  resultado = requests.get(url_pagina)
  sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

  #selecionar los datos del libros
  libros = sopa.select('.product_pod')

  #iterar libros
  for libro in libros:
    #verificar que los libros tenga 4 o 5 estrellas
    if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) !=0:
      
      #guardar titulo en la variable titulo_libro
      titulo_libro = libro.select('a')[1]['title']

      #agregar lirbo a lista
      titulos_rating_alto.append(titulo_libro)
      
for t in titulos_rating_alto:
  print(t)
