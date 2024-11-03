""" 
Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario 
ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina 
una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def identificar_caracteres():
    active = True
    while active:
        try:



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


if __name__ == "__main__":
    main()
