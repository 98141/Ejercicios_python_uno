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