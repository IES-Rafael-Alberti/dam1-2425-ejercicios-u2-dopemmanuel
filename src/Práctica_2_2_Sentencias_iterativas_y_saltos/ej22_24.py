""" 
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""
import os
from ej22_10 import num_primo
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa cuenta la cantidad de números primos ingresados.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def active_prime_zero():
    """Función principal para contar números primos ingresados."""
    nostring = True
    contador_primos = 0
    active = True
    while active:
        try:
            numero = input("Ingrese un número mayor que 1 (0 para terminar): ")
            nostring = False

            if "." in numero:
                raise ValueError("No se permiten decimales aqui...")


            nostring = True
            numero = int(numero)
            nostring = False

            if numero == 0:
                active = False
            else:
                if numero <= 1:
                    raise ValueError("Por favor, ingrese un número mayor que 1.")

            if primo_numero(numero):
                contador_primos += 1


        except ValueError as found:
            if nostring:
                print("ERR0R: Nada de letras")
                print("\n")
                input("Presiona ↩ para intentarlo de nuevo...")
                clear_console()
            else:
                print(found)
                print("\n")
                input("Presiona ↩ para intentarlo de nuevo...")
                clear_console()

def primo_numero(numero: int):
    """Funcion que tiene una funcion llamada:"""
    if numero == 0:
        return None
    else:
        num_primo(numero)

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    active_prime_zero()
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()


if __name__ == "__main__":
    main()
