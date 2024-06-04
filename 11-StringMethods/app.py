texto = "Este es el texto de Jose"
resultado = texto.upper()
resultado = texto.split("t")
resultado = texto.find("q")
resultado = texto.replace("Jose", "Python")
#print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
#print(e)

lista_palabras = ["La","legibilidad","cuenta."]
#print(" ".join(lista_palabras))



url = "https://www.ejemplo.com/path/to/page?query=valor"
url2 = url.split("/")
print(url2[2:3:])