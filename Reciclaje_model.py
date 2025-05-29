from datetime import datetime

class MaterialReciclado:
    def __init__(self, tipo, peso, fecha):
        # Inicializa el material reciclado con tipo, peso y fecha
        self.tipo = tipo
        self.peso = peso
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")

    def calcular_puntos(self):
        # Calcula los puntos base para el material reciclado
        return self.peso * 1

class Plastico(MaterialReciclado):
    def calcular_puntos(self):
        # Calcula los puntos para plástico (2 puntos por unidad de peso)
        return self.peso * 2

class Vidrio(MaterialReciclado):
    def calcular_puntos(self):
        # Calcula los puntos para vidrio (1.5 puntos por unidad de peso)
        return self.peso * 1.5

class Papel(MaterialReciclado):
    def calcular_puntos(self):
        # Calcula los puntos para papel (1.2 puntos por unidad de peso)
        return self.peso * 1.2

class Familia:
    def __init__(self, nombre, integrantes, direccion):
        # Inicializa la familia con nombre, número de integrantes y dirección
        self.nombre = nombre
        self.integrantes = integrantes
        self.direccion = direccion
        self.materiales = []

    def agregar_material(self, material):
        # Agrega un material reciclado a la familia
        self.materiales.append(material)

    def obtener_resumen(self):
        # Obtiene un resumen de los materiales reciclados y el total de puntos
        resumen = []
        total = 0
        for mat in self.materiales:
            puntos = mat.calcular_puntos()
            total += puntos
            resumen.append((mat.tipo, mat.peso, puntos))
        return resumen, total
