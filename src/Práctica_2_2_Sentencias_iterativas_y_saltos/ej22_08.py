""" 
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)
    print("     Este programa pedira al usuario un numero entero para hacer una     ")
    print("        piramide con ello.")
    print("=" * 80)

def pedir_num():
    """La funcion que tiene una vriable que pedira el numero:"""
    nostring = True
    test = True
    while test:
        try:
            num = input("Ingresa un número entero → ")
            nostring = False

            if num == "":
                print("Bye Bye...")
                return None

            if "." in num:
                raise ValueError("Nada de decimales")

            nostring = True
            num = int(num)
            nostring = False

            test = False

        except ValueError as e:
            if nostring:
                print("ERROR: No debería ser letra.")
            else:
                print(e)
    return num

def funcionar(num):
    """Funcion con condiciones que permitira que funcione:"""
    if num is None:
        return None
    else:

        for i in range(1, num + 1):
            for num in range(2 * i - 1, 0, -2):
                print(num, end=" ")
            print()

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def main():
    """Funcion principal:"""
    continues = "y"
    while continues.lower() != "n":

        clear_console()
        introducion()
        print("\n")
        input("Presiona ↩ para continuar...")

        clear_console()

        num = pedir_num()
        if num is None:
            continuar = "n"
        else:

            print("\n")
            funcionar(num)
            print("\n")
            input("Done!!!, presiona ↩ para ir a la siguiente opcion...")

        clear_console()

        continuar = input("Presiona ↩ Para reintentar otra vez..... ")
        if continuar == "":
            clear_console()
            return pedir_num()
        else:
            if continuar == "exit":
                return None

if __name__ == "__main__":
    main()
