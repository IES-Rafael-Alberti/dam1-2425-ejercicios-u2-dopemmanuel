""" 
Leer números enteros de teclado, hasta que el 
usuario ingrese el 0. Finalmente, mostrar la 
sumatoria de todos los números positivos ingresados.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("    Este programa sumara solo los numeros positivos que ingreses, hasta que")
    print("                      coloques el 0.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def funcion():
    """Fncion con condicion:"""
    nostring = True
    suma_total = 0
    active = True
    while active:
        try:
            numero = input("Ingrese un número entero (0 para terminar): → ")
            nostring = False

            if "." in numero:
                raise ValueError("Por favor, ingrese un número entero válido.")

            nostring = True
            numero = int(numero)
            nostring = False

            if numero < 0:
                raise ValueError("Solo se aceptan numeros positivos.")

            if numero == 0:
                active = False

            suma_total += numero

        except ValueError as error:
            if nostring:
                print("ERR0R: No se puede usar cadenas aqui.")
                print("\n")
                input("Presione ↩ para reintentar...")
                clear_console()
            else:
                print(error)
                print("\n")
                input("Presione ↩ para reintentar...")
                clear_console()

    print(f"La suma total de los números ingresados es: {round(suma_total)}")

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()

    funcion()
    print("\n")
    input("Presione ↩ para salir...")

    clear_console()

if __name__ == "__main__":
    main()
