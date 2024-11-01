""" 
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es 
que se ingrese el número -1. Al finalizar, mostrar cuántos de 
los números ingresados por el usuario fueron números pares.
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

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")


if __name__ == "__main__":
    main()
