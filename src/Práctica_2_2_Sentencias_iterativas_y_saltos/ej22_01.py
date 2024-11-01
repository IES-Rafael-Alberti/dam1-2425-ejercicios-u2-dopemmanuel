"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("  Este Programa te pedira una palabra y te la mostrara las veces que quieras.    ")

    print("=" * 80)

def palabra():
    """
    Variables con exepciones:
    """
    nostring = True
    reb = True
    while reb:
        try:
            palabr = input("Coloca la palabra aqui → ")
            nostring = True
            repeat = input("Cuantas veces lo quieres repetir? → ")
            nostring = False

            if "." in repeat:
                raise ValueError("Nada de float.")

            nostring = True
            repeat = int(repeat)
            nostring = False

            if repeat <= 0:
                raise ValueError("No puede ser menor o igual a cero.")

            #sali = input("Quieres salir? (s/n) → ")
            #if sali != "n":
                #reb = False

            reb = False

        except ValueError as e:
            if nostring:
                print("Solo numeros en esta seccion.")
                input("↩ para Reintentar....")
                clear_console()
            else:
                print(e)
                input("↩ para Reintentar....")
                clear_console()



    return {
        "palabr": palabr,
        "repeat": repeat
    }

def veces(datos):
    """
    Funcion con condicion, la variables se almacenaron como cadena
    para usar los datos guardados en la condicion
    """

    repeat = datos["repeat"]
    palabr = datos["palabr"]

    for i in range(repeat):
        i = palabr
        print(i)

def clear_console():
    """Funcion para limpiar la consola:"""
    if os.name == 'nt':
        os.system('cls')

def main():
    """Funcion principal:"""

    clear_console()

    introducion()
    print("\n")
    input("Presiona parar continuar...")
    clear_console()

    numveces = palabra()
    print("\n")
    veces(numveces)


    print("\n")
    input("All done!!....")
    clear_console()

if __name__ == "__main__":
    main()
