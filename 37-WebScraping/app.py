import requests
import bs4    # type: ignore

resultado = requests.get('https://primerreporte.com/2024/06/18/estudiantes-de-arquitectura-uide-loja-en-gira-nacional/')

#trae todo el codigo fuente del sitio
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

#titulo del sitio web
#print(sopa.select('title')[0].get_text())

#traer numero de etiquestas <p>
#print(len(sopa.select('p')))

parrafo = sopa.select('p')[2].get_text()
#print(parrafo)

columna_lateral = sopa.select('.widget-title')

for p in columna_lateral:
  print(p.get_text())


#extraer imagenes
imagenes = sopa.select('.custom-logo')[0]['src']
#print(imagenes)

logo_empresa = requests.get(imagenes)
#print(logo_empresa.content)

#guardar las imagenes
f = open('logo.png', 'wb')
f.write(logo_empresa.content)
f.close()