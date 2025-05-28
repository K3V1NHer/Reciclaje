import re

def mostrar_menu():
    print("\n--- Sistema de Reciclaje por Familias ---")
    print("1. Registrar familia")
    print("2. Registrar material reciclado")
    print("3. Ver resumen por familia")
    print("4. Salir")

def pedir_familia():
    while True:
        nombre = input("Nombre de la familia (solo letras): ").strip()
        if not nombre.isalpha():
            print("Error: el nombre debe contener solo letras sin espacios ni números.")
            continue
        break

    while True:
        try:
            integrantes = int(input("Número de integrantes: "))
            break
        except ValueError:
            print("Error: debe ingresar un número válido para integrantes.")

    direccion = input("Dirección: ")
    return nombre, integrantes, direccion

def seleccionar_familia(familias):
    print("\nFamilias registradas:")
    for i, fam in enumerate(familias):
        print(f"{i + 1}. {fam.nombre}")
    while True:
        try:
            opcion = int(input("Seleccione una familia: "))
            if 1 <= opcion <= len(familias):
                return opcion - 1
            else:
                print("Error: opción fuera de rango.")
        except ValueError:
            print("Error: debe ingresar un número.")

def pedir_material():
    tipos_validos = {"plastico", "vidrio", "papel"}
    while True:
        tipo = input("Tipo de material (plastico, vidrio, papel): ").lower().strip()
        if tipo not in tipos_validos:
            print("Error: solo puede ingresar plastico, vidrio o papel.")
            continue
        break

    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso <= 0:
                print("Error: el peso debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número válido para peso.")

    while True:
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        try:
            # Validar formato fecha
            from datetime import datetime
            datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("Error: la fecha debe estar en formato YYYY-MM-DD.")
    return tipo, peso, fecha

def mostrar_resumen(familia):
    print(f"\nResumen de materiales para {familia.nombre}:")
    resumen, total = familia.obtener_resumen()
    for tipo, peso, puntos in resumen:
        print(f"- {tipo}: {peso} kg, {puntos:.1f} puntos")
    print(f"Total de puntos: {total:.1f}")
