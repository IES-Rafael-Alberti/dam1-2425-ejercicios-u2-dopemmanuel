""" 
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
import os

def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)
    print("     Este programa mostrara la tabla de Multipicar desde el 1 hasta el 10     ")
    print("                 (o para el numero que quieras colocar).     ")
    print("=" * 80)

def fun1():
    """
    Variabl de entrada y condiciones que se asegurara que los ingresado
    cumpla con los requisitos:
    """
    nostring = True
    switch = True

    while switch:
        try:
            num = input("Ingrese el numero: → ")
            nostring = False


            nostring = True
            if "." in num:
                num = float(num)
            else:
                num = int(num)
            nostring = False

            if num < 0:
                raise ValueError("ERROR: el numero debe ser positivo.")

            switch = False
        except ValueError as erros:
            if nostring:
                print("ERROR: No se aceptan letras.")
            else:
                print(erros)
    return num

def fun2(num):

    """Condicion que permitira la multiplicacion"""
    if num != float(num):
        for i in range(1, float(num) + 1.1):
            resultado = num * i
            print(f"{num} x {i} = {resultado:.2f}")
    else:

        for i in range(1, int(num) + 1):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")

def clear_console():
    """Permite limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """Funcion principal"""
    clear_console()

    introducion()
    print("\n")
    input("Presiona ↩  para continuar....")
    clear_console()

    num = fun1()
    print("\n")
    fun2(num)

    print("\n")
    input("Listo!!!, Presiona ↩  para salir.")
    clear_console()

if __name__ == "__main__":
    main()
