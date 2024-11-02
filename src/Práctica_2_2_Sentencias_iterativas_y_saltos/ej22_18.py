""" 
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es 
que se ingrese el número -1. Al finalizar, mostrar cuántos de 
los números ingresados por el usuario fueron números pares.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Me canse de componer titulos.... ヾ(￣▽￣) Bye~Bye~")
    print("")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def suma_digitos(numero):
    """Función que calcula la suma de los dígitos de un número."""
    return sum(int(digito) for digito in str(numero))

def funcion_aj():
    """( •_•)>⌐■-■"""
    contador_pares = 0
    nostring = True
    activador = True
    while activador:
        try:
            numero = input("Ingrese un número entero positivo (-1 para terminar): → ")
            nostring = False

            if "." in numero:
                raise ValueError("ERR0R: ingrese un numero entero, no un decimal.")

            if numero == "":
                raise ValueError("Esto esta vacio, ingresa un numero porfavor.")

            nostring = True
            numero = int(numero)
            nostring = False

            if numero == -1:
                activador = False

            if numero < 0:
                raise ValueError("Por favor, ingrese un número positivo o -1 para terminar.")

            suma = suma_digitos(numero)
            print(f"La suma de los dígitos de {numero} es: {suma}")


            if numero % 2 == 0:
                contador_pares += 1

        except ValueError as errors:
            if nostring:
                print("Error: Debe ingresar un número, no una letra.")
                print("\n")
                input("Presione ↩ para reintentar...")
                clear_console()
            else:
                print(errors)
                print("\n")
                input("Presione ↩ para reintentar...")
                clear_console()

    print(f"\nCantidad de números pares ingresados: {contador_pares}")

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()

    funcion_aj()
    print("\n")
    input("Presione ↩ para salir....")

    clear_console()


if __name__ == "__main__":
    main()
