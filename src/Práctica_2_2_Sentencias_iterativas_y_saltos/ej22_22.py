""" 
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el 
usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def num_digitos_pares_impares():
    nostring = True
    active = True
    while active:
        try:



        except ValueError as found:
            print(found)
            print("\n")
            input("Presiona ↩ para intentarlo de nuevo...")
            clear_console()


def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()


if __name__ == "__main__":
    main()
