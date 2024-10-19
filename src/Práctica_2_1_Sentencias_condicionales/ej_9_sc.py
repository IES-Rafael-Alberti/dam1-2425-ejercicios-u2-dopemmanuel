"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular 
de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""

from ej_1_sc import adult_swim
def saber_edad_promocion(age):
    """Se importa de otra funcion la condicion:""" 
    if age < 4:
        print(f"{adult_swim(age)} Puedes entrar gratis ( •̀ ω •́ )✧ ")

    elif age >= 4:
        print(f"{adult_swim(age)} Son 5€.")

    elif age > 18:
        print(f"{adult_swim(age)} Son 10€.")


def main():
    """VAriables y condiciones con exepciones:"""
    exitts = True
    while exitts:
        try:

            ages = int(input("Cual es tu edad? → "))
            saber_edad_promocion(ages)

            askers = input("Quieres salir? (s/n)→ ")
            if askers != "n":
                exitts = False

        except ValueError:
            print("No se acepta letras...")


if __name__ == "__main__":
    main()