""" 
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total 
a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar 
un 10% de descuento.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("Este programa permite ingresar montos de compra y calcula el total a pagar.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def recibir_montos():
    """Función para recibir los montos de las compras"""
    nostring = True
    total = 0
    active = True
    while active:
        try:
            monto = input("Ingrese el monto de la compra (0 para terminar): ")
            nostring = False

            if monto == "":
                raise ValueError("ERR0R: El campo no debe esta vacio.")

            nostring = True
            monto = float(monto)
            nostring = False

            if monto < 0:
                raise ValueError("ERR0R: Monto no válido. Ingrese un monto positivo.")

            if monto == 0:
                active = False
            total += monto

        except ValueError as found:
            if nostring:
                print("ERR0R: Naa de de letras")
                print("\n")
                input("Presiona ↩  para intentarlo de nuevo..")
            else:
                clear_console()
                print(found)
                print("\n")
                input("Presiona ↩ para intentarlo de nuevo...")

                clear_console()
    return total

def condicion_total(total):
    """Función para recibir el total"""
    if total > 1000:
        descuento = total * 0.1
        total -= descuento
        print(f"\nSe aplicó un descuento del 10% por superar $1000: -${descuento:.2f}")

        print(f"\nEl total a pagar es: ${total:.2f}")
    else:
        print(f"\nEl total a pagar es: ${total:.2f}")

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩ para continuar...")
    clear_console()

    total = recibir_montos()
    condicion_total(total)
    print("\n")
    input("Presione ↩ para salir...")
    clear_console()

if __name__ == "__main__":
    main()
