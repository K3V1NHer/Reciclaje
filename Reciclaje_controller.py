from Reciclaje_model import Familia, Plastico, Vidrio, Papel, MaterialReciclado
import Reciclaje_view as vista

class Controlador:
    def __init__(self):
        # Lista para almacenar las familias registradas
        self.familias = []

    def ejecutar(self):
        # Bucle principal del menú de la aplicación
        while True:
            vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_familia()
            elif opcion == "2":
                self.registrar_material()
            elif opcion == "3":
                self.mostrar_resumenes()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

    def registrar_familia(self):
        # Registra una nueva familia en el sistema
        try:
            nombre, integrantes, direccion = vista.pedir_familia()
            self.familias.append(Familia(nombre, integrantes, direccion))
            print("Familia registrada.")
        except Exception as e:
            print(f"Error: {e}")

    def registrar_material(self):
        # Registra un material reciclado para una familia existente
        if not self.familias:
            print("No hay familias registradas.")
            return
        try:
            idx = vista.seleccionar_familia(self.familias)
            tipo, peso, fecha = vista.pedir_material()

            # Crea el objeto del tipo de material correspondiente
            if tipo == "plastico":
                material = Plastico(tipo, peso, fecha)
            elif tipo == "vidrio":
                material = Vidrio(tipo, peso, fecha)
            else:  # papel
                material = Papel(tipo, peso, fecha)

            # Agrega el material a la familia seleccionada
            self.familias[idx].agregar_material(material)
            print("Material registrado.")
        except Exception as e:
            print(f"Error: {e}")

    def mostrar_resumenes(self):
        # Muestra un resumen de materiales reciclados por cada familia
        if not self.familias:
            print("No hay familias registradas.")
        else:
            for fam in self.familias:
                vista.mostrar_resumen(fam)
