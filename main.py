from conversions.length import *
from conversions.weight import *
from utils import valid_input

def main():
    print("=== Conversor de Unidades ===")
    print("1. Metros a Pies")
    print("2. Kilogramos a Libras")
    print("5. Metros a Centimetros")

    opcion = valid_input("Selecciona una opción: ", int, "Por favor, ingresa un número válido.")

    if opcion == 1:
        metros = valid_input("Ingresa metros: ", float, "Por favor, ingresa un número válido.")
        print(f"{metros} metros = {meters_to_feet(metros):.2f} pies")
    elif opcion == 2:
        kilos = valid_input("Ingresa kilogramos: ", float, "Por favor, ingresa un número válido.")
        print(f"{kilos} kg = {kg_to_pounds(kilos):.2f} libras")
    elif opcion == 5:
        metros = valid_input("Ingresa metros: ", int, "Por favor, ingresa un número válido.")
        print(f"{metros} metros = {meters_to_centimeters(metros):.2f} centimetros")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
