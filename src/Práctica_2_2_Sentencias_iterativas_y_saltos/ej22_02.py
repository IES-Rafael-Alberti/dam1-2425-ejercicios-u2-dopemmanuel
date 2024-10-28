"""
Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def comprobar_numero():
    """
    Variable principal: edad = es str pasara a int si no se detecta algo relacionado con float.
    Variables Booleanas: ↓
    no_letra: Hecho por mario tamayo, y se usa para detectar strings en variables.
    exits: se usara como llave del bucle while, no saldra hasta que se cumpla la condicion.

    Condiciones: ↓
    while: crea un bucle para asegurar que edad sea colocado correctamente.
    if: asegurara que la variable edad cumpla con el requisito.
    try/excepts: atrapa los errores principales, permitiendo cambiar lo que imprime.
    
    """
    no_letra = True # Es Usado para detectar cadenas
    exits = True
    while exits:
        try:
            edad = input("¿Cuantos años tienes? →")
            no_letra = False # Es Usado para detectar cadenas

            if "." in edad:
                raise ValueError("ERROR: Tu edad no puede ser decimal.")

            no_letra = True # Es Usado para detectar cadenas
            edad = int(edad)
            no_letra = False # Es Usado para detectar cadenas

            if edad < 0:
                raise ValueError("ERROR: La edad no puede ser menor que 0")

            exits = False

        except ValueError as e:
            if no_letra:
                print("No se puede usar letras")
            else:
                print(e)
    return edad


def contar_la_edad(edad):
    """De la funcion comprobar numero"""

    hor = ""
    for anios in range(1, int(edad) + 1):
        if anios != int(edad):
            hor += str(anios) + ", "
        else:
            hor = hor.strip(",")
            hor += str(anios)

            print(f"Años cumplidos → {hor.strip(",")[:-4]}.")

def main():
    """
    Funcion principal del programa
    """

    edad = comprobar_numero()
    contar_la_edad(edad)
    print(f"\nY actualmente tienes {edad} años. ")

if __name__ == "__main__":
    main()





    #def contar_la_edad(edad):
    #"""De la funcion comprobar numero"""

    #hor = ""
    #for anios in range(1, int(edad) + 1):
        #hz = hor + str(anios)
        #print(hz, end = ",")
