""" 
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada.
Si el carácter no coincide, indicar que no hay coincidencia en esa posición 
(imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición
se encontró y finalizar la ejecución.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa busca una letra en una frase, carácter por carácter, hasta encontrarla.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def buscar_letra_frase():
    """( •_•)>⌐■-■"""
    inicio = 0
    active = True
    while active:
        try:
            palabra = input("Introduce una cadena de caracteres: → ")
            if palabra == "":
                raise ValueError("ERR0R: esto no debe esta vacio.")

            letra = input("Introduce una letra para buscar: → ")
            if letra == "" or len(letra) > 1:
                raise ValueError("ERROR: Debe ingresar solo una letra.")

            while inicio < len(palabra):
                if palabra[inicio] == letra:
                    print(f"Coincidencia encontrada en la posición {inicio}.")
                    active = False
                else:
                    print(f"No hay coincidencia en la posición {inicio}.")
                inicio += 1

            print("La letra no se encontró en la frase.")
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

    buscar_letra_frase()
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
