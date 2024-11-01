""" 
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
(en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: 
se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
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
