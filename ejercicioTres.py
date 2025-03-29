class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

def mostrarMenu() :
    print("\nInventario de Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir\n")

inventario = []

while True:
    mostrarMenu()
    opcion = input("Seleccione una opción (1-6): ")
    if opcion == '6':
        print("Saliendo del inventario.")
        break

    if opcion in ['1', '2', '3', '4', '5']:
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")

            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.append(producto)
            except ValueError:
                print("Error: Precio y cantidad deben ser números.")

        elif opcion == '2':
            print("Lista de productos:")
            for producto in inventario:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            for producto in inventario:
                if producto.nombre.lower() == nombre_buscar.lower():
                    print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Producto {nombre_buscar} no encontrado.")
        elif opcion == '4':
            nombre_actualizar = input("Ingrese el nombre del producto a actualizar: ")
            for producto in inventario:
                if producto.nombre.lower() == nombre_actualizar.lower():
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    producto.precio = nuevo_precio
                    producto.cantidad = nueva_cantidad
                    print(f"Producto {nombre_actualizar} actualizado.")
                    break
            else:
                print(f"Producto {nombre_actualizar} no encontrado.")
        elif opcion == '5':
            nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
            for producto in inventario:
                if producto.nombre.lower() == nombre_eliminar.lower():
                    inventario.remove(producto)
                    print(f"Producto {nombre_eliminar} eliminado.")
                    break
            else:
                print(f"Producto {nombre_eliminar} no encontrado.")