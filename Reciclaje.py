from datetime import datetime

class MaterialReciclado:
    def __init__(self, tipo, peso, fecha):
        self.tipo = tipo
        self.peso = peso
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")

    def calcular_puntos(self):
        return self.peso * 1

class Plastico(MaterialReciclado):
    def calcular_puntos(self):
        return self.peso * 2

class Vidrio(MaterialReciclado):
    def calcular_puntos(self):
        return self.peso * 1.5

class Papel(MaterialReciclado):
    def calcular_puntos(self):
        return self.peso * 1.2

class Familia:
    def __init__(self, nombre, integrantes, direccion):
        self.nombre = nombre
        self.integrantes = integrantes
        self.direccion = direccion
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def resumen_materiales(self):
        total_puntos = 0
        print(f"\nResumen de materiales para {self.nombre}:")
        for mat in self.materiales:
            puntos = mat.calcular_puntos()
            total_puntos += puntos
            print(f"- {mat.tipo}: {mat.peso} kg, {puntos:.1f} puntos")
        print(f"Total de puntos: {total_puntos:.1f}")

def menu():
    familias = []

    while True:
        print("\n--- Sistema de Reciclaje por Familias ---")
        print("1. Registrar familia")
        print("2. Registrar material reciclado")
        print("3. Ver resumen por familia")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre de la familia: ")
                integrantes = int(input("Número de integrantes: "))
                direccion = input("Dirección: ")
                familias.append(Familia(nombre, integrantes, direccion))
                print("Familia registrada.")
            except ValueError:
                print("Error: El número de integrantes debe ser un número entero.")

        elif opcion == "2":
            if not familias:
                print("No hay familias registradas.")
                continue
            try:
                print("\nFamilias registradas:")
                for i, fam in enumerate(familias):
                    print(f"{i + 1}. {fam.nombre}")
                idx = int(input("Seleccione una familia: ")) - 1
                if idx < 0 or idx >= len(familias):
                    print("Error: Índice fuera de rango.")
                    continue
                tipo = input("Tipo de material (plastico, vidrio, papel): ").lower()
                peso = float(input("Peso (kg): "))
                fecha = input("Fecha (YYYY-MM-DD): ")

                if tipo == "plastico":
                    material = Plastico(tipo, peso, fecha)
                elif tipo == "vidrio":
                    material = Vidrio(tipo, peso, fecha)
                elif tipo == "papel":
                    material = Papel(tipo, peso, fecha)
                else:
                    material = MaterialReciclado(tipo, peso, fecha)

                familias[idx].agregar_material(material)
                print("Material registrado.")
            except ValueError:
                print("Error: Ingrese datos válidos (número, fecha y peso correctos).")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "3":
            if not familias:
                print("No hay familias registradas.")
            else:
                for fam in familias:
                    fam.resumen_materiales()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
