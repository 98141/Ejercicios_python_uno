"""Prueba del ejercicio dos de python"""

print ("Calculo de un area geometrica")
print ("Selecciona el numero de la operacion que deseas realizar")
print ("1. Area de un circulo")
print ("2. Area de un cuadrado")   
print ("3. Area de un rectangulo")

pi = 3.1416

opcion = int(input("Opcion: "))
if opcion == 1:
    radio = float(input("Ingrese el valor del radio: "))
    area = pi * (radio ** 2)
    print (f"El area del circulo es: {area}")
elif opcion == 2:
    lado = float(input("Ingrese el valor de la longitud de un lado: "))
    area = lado ** 2
    print (f"El area del rectangulo es: {area}")
elif opcion == 3:
    longitu = float(input("Ingrese la longitud: "))
    ancho = float(input("Ingrese el ancho: "))
    area = longitu * ancho
    print (f"El area del circulo es: {area}")
else:
    print ("Opcion invalida")

print ("Fin del programa\n")