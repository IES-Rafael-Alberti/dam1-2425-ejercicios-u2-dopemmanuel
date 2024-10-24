"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.






def comprobar_numero():
    Comprobar si
    numero_valido = False
    while not numero_valido:
        num_i = input("Ingresa el número aquí → ")
        try:
            if '.' in num_i:
                raise ValueError("ERROR, no se permiten decimales.")

            num_i = int(num_i)
            if num_i <= 0:
                raise ValueError("ERROR, por favor ingresa un número entero positivo.")

        except ValueError as e:
            print(e)

        numero_valido = True
    return num_i


def numeros_impares(num_i: int):

    Condicion para hacer los numeros impares, extrayendo desde la variable de main:

    num_i = input("Ingresa el numero aqui → ")

    impares = ""
    for inicial in range(1, int(num_i) + 1):
        if inicial % 2 != 0:
            impares += str(inicial) + ","

    return impares[:-1]

def reintentar():
    Para saber si quieres salir del bulce
    intentar = input("Quieres intentarlo de nuevo? (s/n) → ").lower()
    return intentar != "s"

def main():
 
    Variable de tipo any (osea que puede ser int, float str...etc) pedira 
    el numero y luego sera enviada a la condicion dentro de la funcion
    para saber si se cumple:


 
    click = True
    while click:
        num_i = comprobar_numero()
        print(numeros_impares(num_i))

        click = reintentar()

if __name__ == "__main__":
    main()
"""


"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

"""
def comprobar_numero():
    """Permite comprobar la variable"""
    es_str = True
    numero_valido = False

    while not numero_valido:
        try:
            num_i = input("Ingresa el número aquí → ")

            es_str = False
            if "." in num_i:
                raise ValueError("No se permiten decimales.")

            es_str = True
            num_i = int(num_i)
            es_str = False

            if num_i <= 0:
                raise ValueError("ERROR, por favor ingresa un número entero positivo.")

            numero_valido = True
        except ValueError as e:

            if es_str:
                print("No puede ser str")
            else:
                print(f"*ERROR* {e}")


    return num_i


def numeros_impares(num_i: int):
    """
    Condicion para hacer los numeros impares, extrayendo desde la variable de main:
    """

    impares = ""
    for inicial in range(1, int(num_i) + 1):
        if inicial % 2 != 0:
            impares += str(inicial) + ","

    return impares[:-1]

def reintentar():
    """Para saber si quieres salir del bulce"""
    intentar = input("Quieres salir? (s/n) → ").lower()
    return intentar != "s"

def main():
    """
    Contiene en variables las condiciones para ser imprimidas:
    """

    click = True
    while click:
        num_i = comprobar_numero()
        print(numeros_impares(num_i))

        click = reintentar()

if __name__ == "__main__":
    main()
