"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def adult_swim(edad):

    """
    Funcion secundaria que contiene la condcion de la funcion: 
    """
    if edad < 17:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")

    return edad

def main():

    """
    Funcion principal que guarda una pequeña condicion, que al no colocarse
    un numero debe retornar a pedir la edad. 
    Y tambien esta la variable principal
    """
    endup = True

    while endup:
        try:
            edad = int(input("Cual es tu edad? → "))
            adult_swim(edad)

            ask = input("Quieres seguir? (s/n): →").lower()
            if ask != "s" or ask != "si" :
                endup = False

        except ValueError:
            print("Solo se acepta valores de caracter numerico...")

if __name__ == "__main__":
    main()
