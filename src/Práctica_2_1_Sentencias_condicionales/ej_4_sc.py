"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""
def par_inpar(num):
    """Contiene la condicion que permitira comprobar si el numero es par o inpar"""

    if num % 2 == 0:
        print(f"Yep, el {num} es par.")
    else:
        print(f"Nop, el {num} es inpar.")
def main():
    """
    Contiene los datos de la variable junto con el de la fucnion.
    Tambien tiene una exepcion para evitar que se coloquen palabras.
    """

    while True:
        try:
            num = int(input("Ingresa el numero y te dire si es par o inpar → "))

            par_inpar(num)
        except ValueError:
            print("No se permiten ningun caracter que no sea de valor numerico.")

if __name__ == "__main__":
    main()
