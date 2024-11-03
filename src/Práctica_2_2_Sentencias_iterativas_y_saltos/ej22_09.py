""" 
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa hara que almacenes contraseñas en una variable para que")
    print("posteriormente al pedirtela te deje pasar, si no, sera incorrecta.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def contrasenias():
    """Variables para contraseñas:"""

    passwords = ["python","kotlin","mondongo","amongus","contraseña"]
    repeat = True

    print("⟫⟫ Usuario ⟪⟪:")
    usr = input("")
    clear_console()

    while repeat:
        print("⟫⟫ Contrasena ⟪⟪:")
        pswrd = input("").lower()
        clear_console()

        if pswrd not in passwords:
            print("Contraseña incorrecta.")
            print("\n")
            input("Presiona ↩  para reintentar...")

            clear_console()
        else:
            input(f"Contraseña correcta!!!, Bienvenido {usr}")
            repeat = False

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")

    clear_console()

    contrasenias()
    print("\n")
    input("Presiona ↩  para continuar...")

    clear_console()

if __name__ == "__main__":
    main()
