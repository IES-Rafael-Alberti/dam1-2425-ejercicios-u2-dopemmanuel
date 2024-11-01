""" 
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 
3-finalizar programa. A continuación, el usuario debe poder seleccionar 
una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, 
permitiendo volver a elegir. Si elige las opciones 1 ó 2 se 
imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión 
del menú y el programa finalizará.
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
