""" 
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

Modo simple:

{
    print("*\n"),
    print("* *\n"),
    print("* * *\n"),
    print("* * * *\n"),
    print("* * * * *\n"),
}

"""


import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print(" Este programa te pedira un numero entero y te mostrara por pantalla un triangulo ")
    print(" rectangulo. ")

    print("=" * 80)

def num_ini():
    """
    Variabl de entrada y condiciones que se asegurara que los ingresado
    cumpla con los requisitos:
    """
    nostring = True
    switch = True

    while switch:
        try:
            num = input("Ingrese el numero: → ")
            nostring = False

            if num == "":
                return None

            if "." in num:
                raise ValueError("ERROR: no se aceptan decimales.")

            nostring = True
            num = int(num)
            nostring = False

            if num < 0:
                raise ValueError("ERROR: el numero debe ser positivo.")

            switch = False
        except ValueError as erros:
            if nostring:
                print("ERROR: No se aceptan letras.")
            else:
                print(erros)
    return num

def triangulo(num: int):
    """La condicion para el triangulo y un detalle opcional 😂:"""
    if num is None:
        return {
            print("*"),
            print("**"),
            print("***"),
            print("****"),
            print("*****"),
    }
    else:
        for i in range(1, num + 1):
            print("*" * i)

def clear_console():
    """Permite limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """Funcion principal"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()


    num = num_ini()
    print("\n")
    triangulo(num)
    print("\n")
    input("All done!!, presiona ↩ para salir.")

    clear_console()


if __name__ == "__main__":
    main()
