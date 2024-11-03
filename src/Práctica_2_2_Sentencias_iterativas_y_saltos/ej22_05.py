""" 
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print(" Este programa te pedira una cantidad a invertir, el interes ye elnumero de años ")
    print("     y te mostrara el capital obtenido en la inversion de cada año. ")

    print("=" * 80)

def informacion():
    """OK"""
    nostrings = True
    button = True
    user = input("Ingrese un usuario: → ")
    while button:
        try:

            amount = input(f"{user}, Ingresa la cantidad a invertir: → ")
            nostrings = False

            interest = input(f"Ok {user}, ahora ingresa el Interes anual: → ")
            nostrings = False
            if "." in interest:
                raise ValueError("ERROR: nada de decimal.")


            years = input(f"Por ultimo {user}, coloca los años de la inversion: → ")
            nostrings = False
            if "." in years:
                raise ValueError("ERROR: no puede ser decimal.")

            nostrings = True
            amount = float(amount)
            interest = int(interest)
            years = int(years)
            nostrings = False

            button = False


        except ValueError as e:
            if nostrings:
                print("No se aceptan letras.")
                input("Presiona ↩ para reintentar...")

                clear_console()
            else:
                print(e)
                input("Presiona ↩ para reintentar...")

                clear_console()

    return {
        "user": user,
        "amount": amount,
        "interest": interest,
        "years": years
    }

def operacion(data):
    """
    Tomar los datos de la lista que estan asignados como variables para ser usadons
    en la condicion for y en la operacion
    """
    amount = data["amount"]
    interest = data["interest"]
    years = data["years"]

    for year in range(1, years + 1):
        amount *= 1 + interest / 100

    print(f"Capital después de {year} años: {amount:.2f}")

def clear_console():
    """Funcion para limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """DATOS"""

    clear_console()
    introducion()
    print("\n")
    input("Presiona ↩ para continuar...")

    clear_console()

    data = informacion()
    print("\n")
    operacion(data)
    print("\n")
    input("All Done!!, press ↩ for exit.")
    clear_console()

if __name__ == "__main__":
    main()
