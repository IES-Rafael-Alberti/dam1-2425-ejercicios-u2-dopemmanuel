"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def adult_swim(edad: int):

    """
    Funcion secundaria que contiene la condcion de la funcion: 
    """
    if edad < 0:
        print("Eso es imposible...")
    elif edad < 17:
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
    string = True
    endup = True

    while endup:
        try:
            edad = input("Cual es tu edad? → ")

            string = False
            if "." in edad:
                raise ValueError("Desde cuando la edad se representa con decimal?")

            string = True
            edad = int(edad)
            string = False


            adult_swim(edad)

            #ask = input("Quieres salir? (s/n): → ").lower()
            #if ask != "s" or ask != "si" :
                #endup = False

            endup = False

        except ValueError as e:
            if string:
                print("Solo se acepta valores de caracter numerico... osea nada de letras")
            else:
                print(f"{e}")


if __name__ == "__main__":
    main()
