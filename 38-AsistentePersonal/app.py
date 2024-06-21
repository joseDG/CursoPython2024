import pyttsx3 # type: ignore
import speech_recognition as sr  # type: ignore
import pywhatkit # type: ignore
import yfinance as yf # type: ignore
import webbrowser
import datetime
import wikipedia # type: ignore
import pyjokes # type: ignore

#Opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

#escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

  #almacenar recognizer en variable
  r = sr.Recognizer()

  #configurar el microfono de la computadora
  with sr.Microphone() as origin:

    #tiempo de espera
    r.pause_threshold = 0.8

    #informar que comenzo a grabar
    print("ya puedes hablar")

    #guardar lo que escuche como audio
    audio = r.listen(origin)

    try:
      #buscar por google
      pedido = r.recognize_google(audio, language="es-mx")

      #prueba de que pudo ingresar
      print("Dijiste: " + pedido)

      #devolver lo solicitado
      return pedido
    
    #error inesperado
    except :
      print("üps, algo salio mal")

      #devolver el error
      return "sigo esperando"

#funciona para qeu el asistente pueda ser escuchado
def hablar(mensaje):

  engine = pyttsx3.init()
  engine.setProperty('voice', id1)

  #promunciar un mensaje
  engine.say(mensaje)
  engine.runAndWait()

#informe el dia de la semana
def pedir_dia():

  #crear la variable con datos de hoy
  dia = datetime.date.today()
  print(dia)

  #crear variable para el dia de semana
  dia_semana = dia.weekday()
  print(dia_semana)

  #diccionario con nombres de dias
  calendario = {0: 'Lunes',
                1: 'Martes',
                2: 'Miercoles',
                3: 'Jueves',
                4: 'Viernes',
                5: 'Sabado',
                6: 'Domingo',
                }
  #decir el dia de la semana
  hablar(f'Hoy es {calendario[dia_semana]}')

#informar hora
def pedir_hora():
  #crear uan variable con datos de la hora
  hora = datetime.datetime.now()
  hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
  print(hora)

  #decir la hora
  hablar(hora)

# funcion saludo inicial
def saludo_inicial():
  #crear variable con datos de hora
  hora = datetime.datetime.now()
  if hora.hour < 6 or hora.hour > 20:
    momento = "Buenas noches"
  elif 6 <= hora.hour < 13:
    momento = "Buen dia"
  else:
    momento = "Buenas tardes"

  #decir saludo
  hablar(f'{momento}, soy Sabina, tu asistente personal. Porfavor , dime en que te puedo ayudar')

#funcion central de asistente
def pedir_cosas():

  #activar saludo incial
  saludo_inicial()

  #crear una variable de corte
  comenzar = True

  #loop central
  while comenzar:

    #activar el microfono y guardar el pedido en un string
    pedido = transformar_audio_en_texto().lower()

    if 'abrir youtube' in pedido:
      hablar('Con gusto, estoy abriendo youTube')
      webbrowser.open('https://www.youtube.com/')
      continue
    elif 'abrir navegador' in pedido:
      hablar('Claro, estoy en eso')
      webbrowser.open('https://www.google.com.ec/')
      continue
    elif 'que dia es hoy' in pedido:
      pedir_dia()
      continue
    elif 'que hora es' in pedido:
      pedir_hora()
      continue
    elif 'busca en wikipedia' in pedido:
      hablar('Buscando eso en wikipedia')
      pedido = pedido.replace('busca en wikipedia', '')
      wikipedia.set_lang('es')
      resultado = wikipedia.summary(pedido, sentences=1)
      hablar('Wikipedia dice lo siguiente:')
      hablar(resultado)
      continue
    elif 'busca en internet' in pedido:
      hablar('Ya mismo estoy en eso')
      pedido = pedido.replace('busca en internet', '')
      pywhatkit.search(pedido)
      continue
    elif 'reproducir' in pedido:
      hablar('Buena idea, ya comienzo a reproducirlo')
      pywhatkit.playonyt(pedido)
      continue
    elif 'broma' in pedido:
      hablar(pyjokes.get_joke('es'))
      continue
    elif 'adiós' in pedido:
      hablar('Me voy a descanzar, cualquier cosa me avisas')
      break

pedir_cosas()


