print("¡Bienvenido al programa de interactividad en Python!\n")
nombre = input("¡Hola! ¿Cuál es tu nombre? ")
print(f"\n Hola, {nombre}! Bienvenido al programa de operaciones matemáticas.\n")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

suma = num1 + num2
print(f"\n{nombre}, el resultado de la suma es: {suma}\n")

resta = num1 - num2
print(f"{nombre}, el resultado de la resta es: {resta}\n")

multiplicacion = num1 * num2
print(f"{nombre}, el resultado de la multiplicación es: {multiplicacion}\n")

exponente = num1 ** num2
print(f"{nombre}, el resultado de {num1} elevado a {num2} es: {exponente}\n")

cuadrado = num1 ** 2
print(f"{nombre}, el cuadrado de {num1} es: {cuadrado}\n")

cuadrado = num2 ** 2
print(f"{nombre}, el cuadrado de {num2} es: {cuadrado}\n")

if num2 != 0:
    division = num1 / num2
    print(f"{nombre}, el resultado de la división es: {division}\n")
else:
    print(f"{nombre}, no se puede dividir por cero.\n")

if num2 != 0:
    modulo = num1 % num2
    print(f"{nombre}, el resultado del módulo es: {modulo}\n")
else:
    print(f"{nombre}, no se puede realizar el módulo por cero.\n")


if num2 != 0:
    division_entera = num1 // num2
    print(f"{nombre}, el resultado de la división entera es: {division_entera}\n")
else:
    print(f"{nombre}, no se puede realizar la división entera por cero.\n")

print(f"¡Gracias por utilizar el programa de operaciones matemáticas, {nombre}!")

"""
Validacion de datos
"""
print(f"\n{nombre} Ahora vamos a verificar los tipos de datos.\n")

entero = int(input("Introduce un número entero: "))
print(f"El valor ingresado es: {entero}, y su tipo es: {type(entero)}\n")

flotante = float(input("Introduce un número flotante: "))
print(f"El valor ingresado es: {flotante}, y su tipo es: {type(flotante)}\n")

real = float(input("Introduce la parte real del número complejo: "))
imaginario = float(input("Introduce la parte imaginaria del número complejo: "))
complejo = complex(real, imaginario)
print(f"El número complejo ingresado es: {complejo}, y su tipo es: {type(complejo)}\n")

texto = input("Introduce una cadena de texto (puede ser tu nombre o cualquier cosa): ")
print(f"El valor ingresado es: {texto}, y su tipo es: {type(texto)}\n")

num1 = int(input("Introduce un primer número para comparar: "))
num2 = int(input("Introduce un segundo número para comparar: "))
comparacion = num1 == num2
print(f"La comparación {num1} == {num2} es: {comparacion} (Booleano, True o False)\n")