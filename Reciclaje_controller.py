from Reciclaje_model import Familia, Plastico, Vidrio, Papel, MaterialReciclado
import Reciclaje_view as vista  

class Controlador:
    def __init__(self):
        self.familias = []

    def ejecutar(self):
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
        try:
            nombre, integrantes, direccion = vista.pedir_familia()
            self.familias.append(Familia(nombre, integrantes, direccion))
            print("Familia registrada.")
        except ValueError:
            print("Error: número de integrantes inválido.")

    def registrar_material(self):
        if not self.familias:
            print("No hay familias registradas.")
            return
        try:
            idx = vista.seleccionar_familia(self.familias)
            if idx < 0 or idx >= len(self.familias):
                print("Índice fuera de rango.")
                return
            tipo, peso, fecha = vista.pedir_material()

            if tipo == "plastico":
                material = Plastico(tipo, peso, fecha)
            elif tipo == "vidrio":
                material = Vidrio(tipo, peso, fecha)
            elif tipo == "papel":
                material = Papel(tipo, peso, fecha)
            else:
                material = MaterialReciclado(tipo, peso, fecha)

            self.familias[idx].agregar_material(material)
            print("Material registrado.")
        except Exception as e:
            print(f"Error: {e}")

    def mostrar_resumenes(self):
        if not self.familias:
            print("No hay familias registradas.")
        else:
            for fam in self.familias:
                vista.mostrar_resumen(fam)