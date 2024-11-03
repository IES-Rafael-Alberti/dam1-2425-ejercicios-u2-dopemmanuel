""" 
Escribir un programa que pida al usuario una palabra y luego muestre por 
pantalla una a una las letras de la palabra introducida empezando por 
la última.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("          Este programa te pedira una palabra y la mostrara una a una ")
    print("                   por letras, empezando por la ultima.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def input_word():
    """Vaiable con condiciones y try-except:"""
    active = True
    while active:
        try:
            palabra = input("Introduce una cadena de caracteres: → ")

            if palabra == "":
                raise ValueError("ERR0R: esto no debe esta vacio.")

            if "." in palabra:
                raise ValueError("ERR0R: no se aceptan numeros flotantes.")


            active = False

        except ValueError as errors:
            print(errors)
            print("\n")
            input("Presione ↩ para reintentar...")

            clear_console()

    return palabra

def operation(palabra: str):
    """Condicion operacional:"""

    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i] + " " , end="")

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()

    palabra = input_word()
    print("\n")
    operation(palabra)
    print("\n")
    input("Presione ↩ para salir...")

    clear_console()

if __name__ == "__main__":
    main()
