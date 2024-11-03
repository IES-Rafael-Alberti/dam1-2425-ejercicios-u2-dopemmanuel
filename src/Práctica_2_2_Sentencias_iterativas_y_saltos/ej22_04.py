"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
import os

def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("     Este programa te pedira un numero entero positivo y te mostrara ")
    print("       del fin(el numero que colocastes) hasta el 1, osea una cuenta ")
    print("       hacia atras.")
    print("=" * 80)

def pedir_al_usuario_num():
    """
    Funcion con variable y condiciones que se tienen que cumplir:
    """
    no_letra = True
    salida_ra = True
    user = input("Introduzca su usuario: → ")
    while salida_ra:
        try:
            numr = input(f"Bienvenido {user}, ahora ingresa un numero entero: → ")

            no_letra = False
            if "." in numr:
                raise ValueError("Nada de decimales (￣︿￣*()")

            no_letra = True
            numr = int(numr)
            no_letra = False

            salida_ra = False

        except ValueError as e:
            if no_letra:
                print("Tampoco se aceptan letras...")
            else:
                print(e)
    return numr

def numero_ntero(numr: int):

    """Condicion que hara la cuenta hacia atras"""    
    entero = ""
    for inicial in range(int(numr), 0 ,-1):
        entero += str(inicial) + ","

    return entero[:-1]

def clear_console():
    """Funcion para limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """Funcion principal con Variables y dos condiciones:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar....")

    clear_console()


    numr = pedir_al_usuario_num()
    print("\n")
    print(f"{numero_ntero(numr)}.")
    print("\n")
    input("All Done!!, Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
