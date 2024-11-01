""" 
Escribir un programa que pida al usuario una palabra y luego muestre por 
pantalla una a una las letras de la palabra introducida empezando por 
la última.
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
