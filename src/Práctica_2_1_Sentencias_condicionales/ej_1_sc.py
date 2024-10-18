"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""
def adult_swim(edad):

    """Funcion secundaria que contiene la condcion del codigo """
    if edad < 17:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

def main():

    """Fucnion principal"""
    print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.\n")
    edad = int(input("Cual es tu edad? → "))

    while edad != int(edad):
        print("Solo se acepta valores de caracter numerico..")
        return edad

    adult_swim(edad)

if __name__ == "__main__":
    main()
