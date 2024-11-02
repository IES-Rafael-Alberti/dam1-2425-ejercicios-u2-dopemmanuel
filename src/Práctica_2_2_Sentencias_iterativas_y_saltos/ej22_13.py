""" 
Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("        Este prorgrama hara eco a todo lo que le introduzcas, hasta que")
    print("                  le escribas salir, haciendo que termine ")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def eco_mode():
    """Funcion con condicion que hara eco a la palabra:"""
    active = True
    while active:
        frase = input("Introduce algo: ")
        if frase == "salir":
            active = False
        print(frase)

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    eco_mode()


if __name__ == "__main__":
    main()
