import random

valorArt = int(input("Ingrese el valor en USD del articulo encontrado:"))


def tesoroValor(valorArt):
  if valorArt < 2000:
    return print("Es de bajo valor")
  elif valorArt >= 2000:
    return print("Es de alto valor")


tesoroValor(valorArt)

adivinanzas = [
    ("Blanco por dentro, verde por fuera.", "La pera"),
    ("Roja por dentro, verde por fuera.", "La sandía"),
    ("Tiene dientes y no come, tiene cabeza y no es hombre.", "El peine"),
    ("Cinco hermanos en un cuarto, todos muy quietos y callados.",
     "Los dedos"),
    ("Dos hermanitas en un cuarto, una blanca, otra negra.", "La cebolla"),
    ("Largo como un poste, redondo como un queso.", "El pepino"),
    ("Tengo forma de jarra y no soy jarra, tengo asa y no soy taza.",
     "El corazón"), ("Si me nombras, ya no existo.", "El silencio")
]


def resCorrecta(adivinanzas):
  numAdivinanza = random.randint(0, len(adivinanzas) - 1)
  adivinanza = adivinanzas[numAdivinanza]
  print("Adivinanza:", adivinanza[0])
  respuesta = input("Ingrese su respuesta:")
  aux = False

  #el lower es para evitar sensibilidad con las mayus#
  if respuesta.lower() == adivinanza[1].lower():
    print("¡Respuesta correcta!, avance en su aventura")
    return True
  else:
    print("Respuesta incorrecta, intente nuevamente")
    return False

#el while not corresponde a un bucle que se repita cuando se cumpla una condicion q#
#indique falso#
while not resCorrecta(adivinanzas):
    pass  #el pass es simlemente para indicar un bucle que no necesita codigo adentro#


resCorrecta(adivinanzas)
