import random

nombre = input("¿Cómo te llamas? ")
pociones = int(input("Ingrese su cantidad de pociones:"))

print("Su nombre es:", nombre, "Y tiene", pociones, "pociones de todo tipo")

resEnemiga = int(input("Ingrese la cantidad de resistencia de su enemigo:"))
hechizo = int(input("Ingrese el poder de su hechizo:"))


def derrotarEnemigo(resEnemiga, hechizo):
  if resEnemiga < hechizo:
    return print("Si, puede derrotar al enemigo")
  elif resEnemiga > hechizo:
    return print("No, no puede derrotar al enemigo")
  elif resEnemiga == hechizo:
    return print("Estan en condiciones igualitorias")


derrotarEnemigo(resEnemiga, hechizo)

nombre = input("Ingresa el nombre de tu personaje: ")
puntHabilidad = int(input("Ingresa tu puntaje de habilidad:"))

mensajesNom = [
    "Bienvenido a esta aventura mágica,",
    "Prepárate para enfrentar desafíos épicos,",
    "Los peligros te aguardan en cada esquina,",
    "Recuerda que la magia está en tu interior,",
    "Que los hechizos te acompañen,"
]

mensajesHab = [
    "Tu habilidad podría mejorar. ¡Sigue practicando!",
    "Necesitas más entrenamiento para dominar tus habilidades.",
    "Tienes habilidades decentes, pero aún hay margen de mejora.",
    "¡Bien hecho! Tu habilidad es bastante prometedora.",
    "¡Impresionante! Tu habilidad es excepcionalmente alta.",
    "Eres un maestro en tu campo. ¡Sigue así!",
    "Tu habilidad es legendaria. ¡Nadie puede igualarte!"
]


def mensPersonalizados(nombre, puntHabilidad):
  menNombre = random.choice(mensajesNom)
  print(menNombre, nombre)

  menHabilidad = random.choice(mensajesHab)
  print(menHabilidad)


mensPersonalizados(nombre, puntHabilidad)
