""" 
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
(en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: 
se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa encuentra la palabra más larga y cuenta el total de palabras en una frase.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def larga_palabra():
    """Función que solicita una frase y encuentra la palabra más larga."""
    active = True
    while active:
        try:
            frase = input("Introduce una frase: ")

            if not frase.strip():
                raise ValueError("ERROR: La frase no debe estar vacía.")

            palabras = frase.split()
            cantidad_palabras = len(palabras)

            palabra_mas_larga = palabras[0]
            for palabra in palabras:
                if len(palabra) > len(palabra_mas_larga):
                    palabra_mas_larga = palabra

            print(f"\nLa palabra más larga es: '{palabra_mas_larga}'")
            print(f"Cantidad de palabras: {cantidad_palabras}")

            active = False

        except ValueError as found:
            print(found)
            print("\n")
            input("Presiona ↩ para intentarlo de nuevo...")
            clear_console()

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    larga_palabra()
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
