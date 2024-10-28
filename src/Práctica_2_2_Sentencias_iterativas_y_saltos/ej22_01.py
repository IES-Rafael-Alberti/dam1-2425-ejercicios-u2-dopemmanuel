"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def palabra():
    """
    Variables con exepciones:
    """

    reb = True
    palabr = input("Coloca la palabra aqui → ")

    while reb:
        try:

            repeat = input("Cuantas veces lo quieres repetir? → ")

            if "." in repeat:
                raise ValueError("Nada de float.")

            repeat = int(repeat)

            for i in range(repeat):
                i = palabr
                print(i)

            #sali = input("Quieres salir? (s/n) → ")
            #if sali != "n":
                #reb = False

            reb = False

        except ValueError as e:
            print(e)


def main():
    """Comentar"""
    palabra()


if __name__ == "__main__":
    main()
