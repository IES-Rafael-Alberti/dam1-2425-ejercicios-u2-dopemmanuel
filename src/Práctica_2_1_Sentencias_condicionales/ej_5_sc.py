"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

from ej_1_sc import adult_swim
def confirmar_edad_ingresos(age, ingresos):
    """↑ Llamo la funcion que tengo en el ej_01_sc.py, usando la funcion llamada como una variable 
          ↓
    """
    if adult_swim(age) and ingresos >= 1000:
        return True
    else:
        return False


def main():
    """Variables"""
    bucle_continue = True

    while bucle_continue:
        try:
            age = int(input("Cual es tu edad? → "))
            ingresos = float(input("De cuanto son tus ingresos? → "))


            if confirmar_edad_ingresos(age, ingresos):
                print("Hay que tributar chico.")
            else:
                print("No creo que haya que tributar.")

            question = input("Quieres ingresar otra edad e ingresos?(s/n): → ").lower()

            if question != "s":
                bucle_continue = False

        except ValueError:
            print("ERROR 001: solo se permiten caracteres numericos.")


if __name__ == "__main__":
    main()
