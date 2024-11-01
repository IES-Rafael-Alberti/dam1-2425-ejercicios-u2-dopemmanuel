"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("     Este programa te pedira un numero entero positivo y te mostrara ")
    print("       por pantalla los numeros impares desde el 1 hasta el numero ")
    print("       que colocastes.")
    print("=" * 80)

def comprobar_numero():
    """Variabbles con un par de condiciones:"""
    es_str = True
    numero_valido = False

    while not numero_valido:
        try:
            num_i = input("Ingresa el número aquí → ")
            es_str = False

            if num_i == "":
                return None

            if "." in num_i:
                raise ValueError("No se permiten decimales.")

            es_str = True
            num_i = int(num_i)
            es_str = False

            if num_i <= 0:
                raise ValueError("ERROR, por favor ingresa un número entero positivo.")

            numero_valido = True
        except ValueError as e:

            if es_str:
                clear_console()
                print("ERROR: nada de letras...")
                print("\n")
                input("Press ↩  for retry...")
                clear_console()
            else:
                clear_console()
                print(f"*ERROR* {e}")
                print("\n")
                input("Press ↩  for retry...")
                clear_console()


    return num_i

def numeros_impares(num_i: int):
    """
    Condicion para hacer los numeros impares, extrayendo desde la variable de main:
    """
    if num_i is None:
        return None
    else:
        impares = ""
    for inicial in range(1, int(num_i) + 1):
        if inicial % 2 != 0:
            impares += str(inicial) + ","

    return impares[:-1]

#def reintentar():
    #"""Para saber si quieres salir del bulce"""
    #intentar = input("Quieres salir? (s/n) → ").lower()
    #return intentar != "s"

def clear_console():
    """Funcion para limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """
    Contiene en variables las condiciones para ser imprimidas:
    """
    clear_console()

    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    click = True
    while click:
        num_i = comprobar_numero()
        print("\n")
        print(f"{numeros_impares(num_i)}.")

        click = False
        print("\n")
        input("Donee!!, Presione ↩ para salir....")
        clear_console()

if __name__ == "__main__":
    main()
