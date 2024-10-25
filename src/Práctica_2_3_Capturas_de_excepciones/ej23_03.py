""" 
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
Deberá solicitar el número hasta introducir uno correcto.
"""

def numero_ntero(numr):

    """OK"""    
    entero = ""
    for inicial in range(int(numr), 0 ,-1):
        entero += str(inicial) + ","

    return entero[:-1]

def main():

    """OKS"""
    no_letra = True
    salida_ra = True
    while salida_ra:
        try:
            numr = input("Ingresa un numero entero → ")

            no_letra = False
            if "." in numr:
                raise ValueError("Nada de decimales (￣︿￣*()")

            no_letra = True
            numr = int(numr)
            no_letra = False

            print(numero_ntero(numr))

            #askers = input("Quieres salir? (s/n) → ")
            #if askers != "s":
                #salida_ra = False

            salida_ra = False

        except ValueError as e:
            if no_letra:
                print("Tampoco se aceptan letras...")
            else:
                print(f"{e} ")

if __name__ == "__main__":
    main()
