"""
Escribir un programa en el que se pregunte al usuario 
por una frase y una letra, y muestre por pantalla el 
número de veces que aparece la letra en la 
frase.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("       Este progrrama se encarga de mostrarte el numero de veces que se repite la letra")
    print("                       especifica de la palabra que escriba.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def input_word():
    """Vaiable con condiciones y try-except:"""
    active = True
    while active:
        try:
            palabra = input("Introduce una cadena de caracteres: → ")

            if palabra == "":
                raise ValueError("ERR0R: esto no debe esta vacio.")

            active = False

        except ValueError as errors:
            print(errors)
            print("\n")
            input("Presione ↩  para reintentar...")
            clear_console()

    return palabra

def encontrar_letra(palabra: str):
    """Esta funcion encontrara los detalles de la palabra:"""
    verdad = True
    while verdad:
        try:
            letras = input(f"OK, la palabra {palabra} ¿Que letra quieres encontrar? → ").upper()
            palabra.find(letras)

            if letras == "":
                raise ValueError("ERR0R: algo se debe buscar... menos el vacio")

            print("\n")
            print(f"Hay {palabra.count(letras)} letras -{letras.upper()}- en la palabra {palabra}.")

            verdad = False

        except ValueError as errors:
            print(errors)
            print("\n")
            input("Presione ↩ para reintentar...")
            clear_console()

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩  para continuar...")

    clear_console()

    palabra = input_word()
    encontrar_letra(palabra)
    print("\n")
    input("Presione ↩  para salir...")
    clear_console()

if __name__ == "__main__":
    main()
