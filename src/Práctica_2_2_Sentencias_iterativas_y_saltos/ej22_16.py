""" 
Leer números enteros positivos de teclado, 
hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado.
"""
import os

def introducion():
    """Función para el título."""
    print("=" * 80)
    print("          Este programa sumará los números que coloques")
    print("               y te dirá cuál es el número mayor.")
    print("=" * 80)

def clear_console():
    """Esta función permite limpiar la consola."""
    if os.name == 'nt':
        os.system('cls')

def funcion():
    """Función que lee números, calcula la suma y encuentra el mayor número ingresado."""
    mayor = None
    suma_total = 0
    active = True

    while active:
        try:
            numero = input("Ingrese un número entero positivo (0 para terminar): → ")

            if "." in numero:
                raise ValueError("Por favor, ingrese un número entero válido.")

            numero = int(numero)


            if numero < 0:
                raise ValueError("Solo se aceptan números positivos.")

            if numero == 0:
                active = False
                continue

            # Actualizar el número mayor si corresponde
            if mayor is None or numero > mayor:
                mayor = numero

            suma_total += numero

        except ValueError as error:
            print(f"Error: {error}")
            input("Presione ↩ para reintentar...")
            clear_console()

    print(f"\nLa suma total de los números ingresados es: {suma_total}")
    if mayor is not None:
        print(f"El mayor número ingresado fue: {mayor}")

def main():
    """Función principal."""
    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()
    funcion()
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
