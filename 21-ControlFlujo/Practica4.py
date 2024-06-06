print("Bienvenidos ala montanaRusa")
altura = int(input("Cual es tu altura en cm? "))

if altura >= 120:
  print("Tu puedes usar la montanaRusa!")
  edad = int(input("Cual es tu edad? "))
  if edad <= 12:
    print("pagar $5")
  elif edad <= 18:
    print("pagar $7")
  elif edad >= 20:
    print("pagar $12")
else:
  print("Lo siento tu no puedes subir ala montana rusa")