class Nota:
    def __init__(self, titulo, contenido, categoria, fecha):
        self.titulo = titulo
        self.contenido = contenido
        self.categoria = categoria
        self.fecha = fecha

class SistemaNotas:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, titulo, contenido, categoria, fecha):
        nueva_nota = Nota(titulo, contenido, categoria, fecha)
        self.notas.append(nueva_nota)
        print("Nota agregada exitosamente.")

    def listar_notas(self):
        if not self.notas:
            print("No hay notas guardadas.")
        for idx, nota in enumerate(self.notas, start=1):
            print(f"{idx}. {nota.titulo} - {nota.categoria} - {nota.fecha}")

    def buscar_nota(self, palabra_clave):
        resultados = [nota for nota in self.notas if palabra_clave.lower() in nota.titulo.lower() or palabra_clave.lower() in nota.contenido.lower()]
        if not resultados:
            print("No se encontraron notas con esa palabra clave.")
        for nota in resultados:
            print(f"Título: {nota.titulo}, Categoría: {nota.categoria}, Fecha: {nota.fecha}\nContenido: {nota.contenido}")

    def eliminar_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo.lower() == titulo.lower():
                self.notas.remove(nota)
                print("Nota eliminada exitosamente.")
                return
        print("No se encontró una nota con ese título.")

    def modificar_nota(self, titulo, nuevo_contenido):
        for nota in self.notas:
            if nota.titulo.lower() == titulo.lower():
                nota.contenido = nuevo_contenido
                print("Nota actualizada exitosamente.")
                return
        print("No se encontró una nota con ese título.")

sistema = SistemaNotas()
while True:
    print("\n1. Agregar Nota")
    print("2. Listar Notas")
    print("3. Buscar Nota")
    print("4. Modificar Nota")
    print("5. Eliminar Nota")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        titulo = input("Título: ")
        contenido = input("Contenido: ")
        categoria = input("Categoría: ")
        fecha = input("Fecha (DD/MM/AAAA): ")
        sistema.agregar_nota(titulo, contenido, categoria, fecha)
    elif opcion == "2":
        sistema.listar_notas()
    elif opcion == "3":
        palabra_clave = input("Ingrese palabra clave: ")
        sistema.buscar_nota(palabra_clave)
    elif opcion == "4":
        titulo = input("Ingrese el título de la nota a modificar: ")
        nuevo_contenido = input("Ingrese el nuevo contenido: ")
        sistema.modificar_nota(titulo, nuevo_contenido)
    elif opcion == "5":
        titulo = input("Ingrese el título de la nota a eliminar: ")
        sistema.eliminar_nota(titulo)
    elif opcion == "6":
        print("Saliendo del sistema de notas.")
        break
    else:
        print("Opción no válida, intente de nuevo.")