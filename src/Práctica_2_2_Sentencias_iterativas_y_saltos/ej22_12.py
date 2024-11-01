"""
Escribir un programa en el que se pregunte al usuario 
por una frase y una letra, y muestre por pantalla el 
número de veces que aparece la letra en la 
frase.
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
