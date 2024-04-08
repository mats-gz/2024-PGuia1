#para evitar futuros errores, poner las variables que funcionan como dividiendo en el 
#parametro de la funcion, en lugar de declararlas afuera, y que su valor sea declarado 
#en el print


def tiempoViaje(distTotal, velNave):
  segViaje = distTotal / velNave
  return segViaje

print("El tiempo total de viaje es:" , tiempoViaje(5000, 300), "segundos")

base = int(input("Ingrese el valor de la base: "))
altura = int(input("Ingrese el valor de la altura: "))

def areaTriangulo(base, altura):
  area = (base * altura) / 2
  return area

print("El area de la superficie es: ", areaTriangulo(base, altura), "centrimetos cuadrados")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calcular_combinaciones(personas, tamEquipo):
    if personas < tamEquipo:
        return 0
    else:
        return factorial(personas) // (factorial(tamEquipo) * factorial(personas - tamEquipo))

print("El número de combinaciones es:", calcular_combinaciones(10, 2))