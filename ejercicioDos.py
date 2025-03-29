class Contacto:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    
def mostrarMenu():
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir\n")

Contactos = []

while True:
    mostrarMenu()
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == '5':
        print("Saliendo de la agenda.")
        break
    if opcion in ['1', '2', '3', '4']:
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el telefono del contacto: ")
            nuevo_contacto = Contacto(nombre, telefono)
            Contactos.append(nuevo_contacto)
            print(f"Contacto {nombre} agregado.")
        elif opcion == '2':
            print("Lista de contactos:")
            for contacto in Contactos:
                print(contacto)
        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
            encontrado = False
            for contacto in Contactos:
                if contacto.nombre.lower() == nombre_buscar.lower():
                    print(contacto)
                    encontrado = True
                    break
            if not encontrado:
                print(f"Contacto {nombre_buscar} no encontrado.")
        elif opcion == '4':
            nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
            for contacto in Contactos:
                if contacto.nombre.lower() == nombre_eliminar.lower():
                    Contactos.remove(contacto)
                    print(f"Contacto {nombre_eliminar} eliminado.")
                    break
            else:
                print(f"Contacto {nombre_eliminar} no encontrado.")
    else:
        print("Opción no válida. Intente de nuevo.")