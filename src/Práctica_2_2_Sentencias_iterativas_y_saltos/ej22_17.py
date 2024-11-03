""" 
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""
import os
def introduccion():
    """Función para el título."""
    print("=" * 80)
    print("        El programa leerá un número entero positivo desde el input")
    print("               e imprimirá la suma de los dígitos.")
    print("=" * 80)

def clear_console():
    """Esta función permite limpiar la consola."""
    if os.name == 'nt':
        os.system('cls')

def suma_digitos():
    """Función que lee un número positivo y calcula la suma de sus dígitos."""
    nostring = True
    active = True
    while active:
        try:
            numero = input("Ingrese un número entero positivo: ")
            nostring = False

            nostring = True
            numero = int(numero)
            nostring = False


            if numero < 0:
                raise ValueError("Error: El número debe ser positivo.")

            active = False

        except ValueError as errors:
            if nostring:
                print("Error: Por favor nada de letras, solo numeros.")
            else:
                print(errors)

    suma = sum(int(digito) for digito in str(numero))
    print(f"La suma de los dígitos de {numero} es: {suma}")

def main():
    """Función principal."""
    clear_console()
    introduccion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    suma_digitos()
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
