"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

from ej21_01 import adult_swim
def confirmar_edad_ingresos(age, ingresos):
    """↑
    Llamo la funcion que tengo en el ej_01_sc.py, usando la funcion llamada como una variable 
       ↓
    """

    if adult_swim(age) < 16 and ingresos > 1000 or ingresos < 1000:
        return False
    else:
        return True

def confirmar_tributo(age, ingresos):
    """
    Confirmara si va a tributar:
    """
    if confirmar_edad_ingresos(age, ingresos):

        print("Hay que tributar chico.")
    else:
        print("No creo que haya que tributar.")

def main():
    """Variables, una contiene true, dos seran de entrada y la ultima de salida:"""
    no_str = True
    bucle_continue = True

    while bucle_continue:
        try:
            age = input("Cual es tu edad? → ")
            no_str = False



            if "." in age:
                raise ValueError("La edad no es decimal, Intentalo de nuevo.")

            ingresos = input("De cuanto son tus ingresos? → ")


            no_str = True
            age = int(age)
            ingresos = float(ingresos)
            no_str = False

            confirmar_tributo(age, ingresos)

            #question = input("Quieres ingresar otra edad e ingresos?(s/n): → ").lower()
            #if question != "s":
                #bucle_continue = False

            bucle_continue = False

        except ValueError as e:
            if no_str:
                print("ERROR 001: solo se permiten caracteres numericos.")
            else:
                print(f"{e}")


if __name__ == "__main__":
    main()
