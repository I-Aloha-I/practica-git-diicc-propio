from conversions.length import *
from conversions.weight import *
from conversions.time import *
from utils import valid_input

def main():
    print("=== Conversor de Unidades ===")
    print("1. Metros a Pies")
    print("2. Kilogramos a Libras")
    print("3. Minutos a Segundos")

    opcion = valid_input("Selecciona una opción: ", int, "Por favor, ingresa un número válido.")

    if opcion == 1:
        metros = valid_input("Ingresa metros: ", float, "Por favor, ingresa un número válido.")
        print(f"{metros} metros = {meters_to_feet(metros):.2f} pies")
    elif opcion == 2:
        kilos = valid_input("Ingresa kilogramos: ", float, "Por favor, ingresa un número válido.")
        print(f"{kilos} kg = {kg_to_pounds(kilos):.2f} libras")
    elif opcion == 3:
        min = valid_input("Ingresa minutos: ", float, "Por favor, ingresa un número válido.")
        print(f"{min} minutos = {min_to_sec(min):.2f} segundos")
    elif opcion == 4:
        hour = valid_input("Ingresa horas: ", float, "Por favor, ingresa un número válido.")
        print(f"{hour} horas = {hour_to_min(hour):.2f} minutos")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
