print("¡Bienvenido al programa de interactividad en Python!")
nombre = input("¡Hola! ¿Cuál es tu nombre? ")
print(f"Hola, {nombre}! Bienvenido al programa de operaciones matemáticas.\n")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
print(f"\n{nombre}, el resultado de la suma es: {suma}")

resta = num1 - num2
print(f"{nombre}, el resultado de la resta es: {resta}")

multiplicacion = num1 * num2
print(f"{nombre}, el resultado de la multiplicación es: {multiplicacion}")

exponente = num1 ** num2
print(f"{nombre}, el resultado de {num1} elevado a {num2} es: {exponente}")

cuadrado = num1 ** 2
print(f"{nombre}, el cuadrado de {num1} es: {cuadrado}")

if num2 != 0:
    division = num1 / num2
    print(f"{nombre}, el resultado de la división es: {division}")
else:
    print(f"{nombre}, no se puede dividir por cero.")

if num2 != 0:
    modulo = num1 % num2
    print(f"{nombre}, el resultado del módulo es: {modulo}")
else:
    print(f"{nombre}, no se puede realizar el módulo por cero.")

if num2 != 0:
    division_entera = num1 // num2
    print(f"{nombre}, el resultado de la división entera es: {division_entera}")
else:
    print(f"{nombre}, no se puede realizar la división entera por cero.\n")

print("¿Qué te gustaría hacer ahora?")
print("1. Verificar tipos de datos.")
opcion = input("Ingresa 1 para seleccionar esta opción: ")

if opcion == "1":
    entero = int(input("Introduce un número entero: "))
    print(f"El valor ingresado es: {entero}, y su tipo es: {type(entero)}")

    flotante = float(input("Introduce un número flotante: "))
    print(f"El valor ingresado es: {flotante}, y su tipo es: {type(flotante)}")

    real = float(input("Introduce la parte real del número complejo: "))
    imaginario = float(input("Introduce la parte imaginaria del número complejo: "))
    complejo = complex(real, imaginario)
    print(f"El número complejo ingresado es: {complejo}, y su tipo es: {type(complejo)}")

    texto = input("Introduce una cadena de texto (puede ser tu nombre o cualquier cosa): ")
    print(f"El valor ingresado es: {texto}, y su tipo es: {type(texto)}")

    num1 = int(input("Introduce un primer número para comparar: "))
    num2 = int(input("Introduce un segundo número para comparar: "))
    comparacion = num1 == num2
    print(f"La comparación {num1} == {num2} es: {comparacion} (Booleano, True o False)")
else:
    print("Opción no válida. Por favor ingresa 1 para seleccionar una opción.")
