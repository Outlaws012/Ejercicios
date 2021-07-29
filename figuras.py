import math

print("Áreas de figuras geométricas")
print("1. Cuadrado.\n2. Círculo.\n3. Tríangulo\n4.Rectángulo")
figura = int(input("Escoja la figura: "))

def triangulo_rectangulo(figuraG, b, h):
  if figuraG == 3:
    area = (b*h)/2
    print("El area del triangulo es: ", area)
  elif figuraG == 4:
    area = (b*h)
    print("El area del rectangulo es: ", area)

if figura == 1:
  l = int(input("Ingrese el lado: "))
  area = l**2
  print("El area del cuadrado es: ", area)

if figura == 2:
  r = int(input("Ingrese el radio: "))
  area = math.pi*r**2
  print("El area del círculo es: ", area)

if figura == 3:
  b = int(input("Ingrese la base: "))
  h = int(input("Ingrese la altura: "))
  triangulo_rectangulo(3, b, h)

if figura == 4:
  b = int(input("Ingrese la base: "))
  h = int(input("Ingrese la altura: "))
  triangulo_rectangulo(4, b, h)
