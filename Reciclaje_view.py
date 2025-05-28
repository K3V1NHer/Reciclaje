def mostrar_menu():
    print("\n--- Sistema de Reciclaje por Familias ---")
    print("1. Registrar familia")
    print("2. Registrar material reciclado")
    print("3. Ver resumen por familia")
    print("4. Salir")

def pedir_familia():
    nombre = input("Nombre de la familia: ")
    integrantes = int(input("Número de integrantes: "))
    direccion = input("Dirección: ")
    return nombre, integrantes, direccion

def seleccionar_familia(familias):
    print("\nFamilias registradas:")
    for i, fam in enumerate(familias):
        print(f"{i + 1}. {fam.nombre}")
    return int(input("Seleccione una familia: ")) - 1

def pedir_material():
    tipo = input("Tipo de material (plastico, vidrio, papel): ").lower()
    peso = float(input("Peso (kg): "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    return tipo, peso, fecha

def mostrar_resumen(familia):
    print(f"\nResumen de materiales para {familia.nombre}:")
    resumen, total = familia.obtener_resumen()
    for tipo, peso, puntos in resumen:
        print(f"- {tipo}: {peso} kg, {puntos:.1f} puntos")
    print(f"Total de puntos: {total:.1f}")
