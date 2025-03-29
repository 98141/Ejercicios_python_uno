class Tarea:
    def __init__(self, titulo, descripcion, estado='pendiente'):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def actualizar_estado(self):
        self.estado = 'completada'

    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}\n"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        self.tareas.append(Tarea(titulo, descripcion))
        print("Tarea añadida con éxito.\n")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.\n")
        else:
            for tarea in self.tareas:
                print(tarea)

    def buscar_tarea(self):
        titulo = input("Ingrese el título de la tarea a buscar: ").strip().lower()
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo:
                print(tarea)
                return tarea
        print("Tarea no encontrada.\n")
        return None

    def actualizar_estado_tarea(self):
        tarea = self.buscar_tarea()
        if tarea:
            tarea.actualizar_estado()
            print("Estado actualizado a 'completada'.\n")

    def actualizar_descripcion_tarea(self):
        tarea = self.buscar_tarea()
        if tarea:
            nueva_desc = input("Ingrese la nueva descripción: ")
            tarea.actualizar_descripcion(nueva_desc)
            print("Descripción actualizada con éxito.\n")

    def eliminar_tarea(self):
        titulo = input("Ingrese el título de la tarea a eliminar: ").strip().lower()
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo:
                self.tareas.remove(tarea)
                print("Tarea eliminada con éxito.\n")
                return
        print("Tarea no encontrada.\n")

    def ejecutar(self):
        while True:
            print("\nSistema de Gestión de Tareas")
            print("1. Agregar tarea")
            print("2. Mostrar todas las tareas")
            print("3. Buscar tarea por título")
            print("4. Actualizar estado de una tarea")
            print("5. Actualizar descripción de una tarea")
            print("6. Eliminar tarea")
            print("7. Salir")
            
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.agregar_tarea()
                elif opcion == 2:
                    self.mostrar_tareas()
                elif opcion == 3:
                    self.buscar_tarea()
                elif opcion == 4:
                    self.actualizar_estado_tarea()
                elif opcion == 5:
                    self.actualizar_descripcion_tarea()
                elif opcion == 6:
                    self.eliminar_tarea()
                elif opcion == 7:
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida, intente nuevamente.\n")
            except ValueError:
                print("Error: Ingrese un número válido.\n")

if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.ejecutar()
