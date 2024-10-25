"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""
def tramos_impositivos(renta):
    """Usar ifs para especificar cada cifra de renta anual:"""

    if renta <= 10000:
        impositivo = 5
        return impositivo

    elif renta <= 20000:
        impositivo = 15
        return impositivo

    elif renta <= 35000:
        impositivo = 20
        return impositivo

    elif renta <= 60000:
        impositivo = 30
        return impositivo

    elif renta > 60000:
        impositivo = 45
        return impositivo


def main():
    """Contiene las variables y puede que alguna condicion"""
    salida = True
    while salida:
        try:

            renta = input("De cuanto es su renta anual? → ")
            renta = int(renta)
            print(f"Del impositivo te corresponde el {tramos_impositivos(renta)} %.")

            #quitt = input("Quieres consultar otra vez? (s/n): → ")
            #if quitt != "s":
                #salida = False
            salida = False
        except ValueError:
            print("Recuerda, solo valor numerico si no colocas valor numerico no funcionara...")


if __name__ == "__main__":
    main()
