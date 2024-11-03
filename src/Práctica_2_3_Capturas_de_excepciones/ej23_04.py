"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, 
mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

def captura_exepciones():
    """
    Esta funcion contiene variables, dos condiciones una dentro de otra
    y exeptiones:
    """
    noletras = True
    salid = True
    while salid:
        try:
            nums = input("Ingresa el numero aqui → ")
            noletras = False

            if "." in nums:
                raise ValueError("La entrada no es correcta.")

            noletras = True
            nums = int(nums)
            noletras = False

            #salida = input("¿Reintentar? (s/n) → ")
            #if salida != "n":
                #salid = False

            salid = False

        except ValueError as e:
            if noletras:
                print("Nada de letras, solo numeros.")
            else:
                print(f"{e}")

    return nums

def main():
    """La funcion main solo imprimira el resultado"""

    print(f"Esta correcto, {captura_exepciones()} es el numero entero.")

if __name__ == "__main__":
    main()
