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

    def obtener_resumen(self):
        resumen = []
        total = 0
        for mat in self.materiales:
            puntos = mat.calcular_puntos()
            total += puntos
            resumen.append((mat.tipo, mat.peso, puntos))
        return resumen, total
