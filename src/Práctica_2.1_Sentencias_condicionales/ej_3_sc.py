"""Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero 
el programa debe mostrar un error."""


def numero_divisores(num1, num2):
    """Condiciones"""

    if num1 == 0 or num2 == 0:
        return False
    else:
        division = num1 / num2
        print(f"{num1} entre {num2} da {round(division)}")
        return True
    
def confirmacion(confirmar):
    
    """Hola"""
    if confirmar is True:
        return True
    else:
        return False


def main():

    """Variables y condiciones"""
    num1 = int(input("Ingrese el primer numero → "))
    num2 = int(input("Ingrese el segundo numero → "))


    confirmar = numero_divisores(num1, num2)

    while confirmacion(confirmar) == numero_divisores(num1, num2):

        print("Eeo Compadre, es imposible dividir entre cero")
        num1 = int(input("Ingrese el primer numero → "))

if __name__== "__main__":
    main()