def suma (a, b):
    return a + b

def resta (a, b):
    return a - b


while True:
    mostarMenu()
    opcion = input("Seleccione una opción (1-5): \'n")
    if opcion == '5':
        print("Saliendo de la calculadora.")
        break
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {division(num1, num2)}")
            
    else:
        print("Opción no válida. Intente de nuevo.")
# Fin del código esperar cambios de definicion
