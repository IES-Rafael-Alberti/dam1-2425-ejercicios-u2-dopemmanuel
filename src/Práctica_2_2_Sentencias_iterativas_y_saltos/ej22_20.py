""" 
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada.
Si el carácter no coincide, indicar que no hay coincidencia en esa posición 
(imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición
se encontró y finalizar la ejecución.
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
