""" 
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa te pide un numero y te dice si es primo o no.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def pedir_num():
    """Funcion con variables:"""
    nostring = True
    switch = True
    user = input("Usuario: ")
    while switch:
        try:
            num = input(f"Hola {user}!! ingresa el numero entero: → ")
            nostring = False

            if num == "":
                raise ValueError("ERR0R: Esto no debe estar vacio.")

            if "." in num:
                raise ValueError("ERR0R: No se permiten decimales.")

            nostring = True
            num = int(num)
            nostring = False

            switch = False

        except ValueError as errors:
            if nostring:
                print("ERROR: Solo caracter numerico.")
                input("Pressiona ↩  para intentarlo de nuevo...")
                clear_console()
            else:
                print(errors)
                input("Pressiona ↩  para intentarlo de nuevo...")
                clear_console()
    return num

def num_primo(num: int):
    """Verifica si el valor es par o inpar"""
    if num <= 1:
        print(f"El {num} No es Primo.\n")
    if num <= 3:
        print(f"El {num} es Primo.\n")
    if num % 2 == 0:
        print(f"El {num} no es primo.\n")

    # Opcional: sirve para identificar los divisores impares hasta la raíz cuadrada de num
    for i in range(3, int(num) + 1, 2):
        if num % i == 0:
            print(f"El {i} No es primo.")
        else:
            print(f"El {i} es primo")

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    num = pedir_num()
    print("\n")
    print("Resultados")
    print("––" * 10)
    num_primo(num)
    print("––" * 10)
    print("\n")
    input("Presione ↩  para salir...")

    clear_console()



if __name__ == "__main__":
    main()
