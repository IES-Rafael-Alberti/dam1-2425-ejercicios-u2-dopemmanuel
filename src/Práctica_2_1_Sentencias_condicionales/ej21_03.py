"""Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero 
el programa debe mostrar un error."""

def numero_divisores(num1, num2):

    """
    Condiciones para comprobar y evitar que las variables num1 y num2 sean igual a 0
    afirmandolos con true y false.
    """

    if num1 == 0:
        print("Pana, hay un pequeño error aqui, el primer numero no puede ser cero.")
        return False
    else:
        division = num1 / num2
        print(f"{num1} entre {num2} da {division:.2f}")
        return True

def main():

    """
    Variables num1 y num2 que son tipo int y que va a almacenar los numeros a dividir 
    y con una condicion con exepcion, y para salir de ella una variables llamada solo_numero sera true
    en el caso de que cuando nos pregunte si queremos salir debemos de colocar algo distinto que si: 
    """
    cadena = True
    solo_numero = True
    while solo_numero:
        try:
            num1 = input("Ingrese el primer numero → ")
            num2 = input("Ingrese el segundo numero → ")

            cadena = False

            cadena = True

            num1 = int(num1)
            num2 = int(num2)
            cadena = False

            while not numero_divisores(num1, num2):
                num1 = int(input("Ingrese el primer numero que no sea 0 → "))

            #salir = input("Quieres salir? (s/n) → ")
            #if salir != "n":
                #solo_numero = False

            solo_numero = False

        except ValueError:
            if cadena:
                print("Pana!! Nada de letras... solo caracter numerico.")



if __name__== "__main__":
    main()
