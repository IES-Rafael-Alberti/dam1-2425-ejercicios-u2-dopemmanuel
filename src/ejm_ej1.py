"""
OK
"""
def pedir_edad() -> str:

    """
    Pide la edad al usuario y devuelve una cadena con los años cumplidos.
    """
    while True:
        try:
            edad = input("Ingresa tu edad → ")
            edad = int(edad)

            if edad < 0 or edad > 125:
                raise ValueError("Eso es imposible.")

            rango = ""
            for inicio in range(1, edad + 1):
                rango += str(inicio) + " "

            return rango

        except ValueError:
            print("Solo se aceptan números enteros entre 0 y 125, tambien no puede estar vacio.")


def mostrar_anios_cumplidos(): 
    """
    Muestra los años cumplidos en formato de rango.
    """
    print(f"Tu edad desde aqui → {pedir_edad()} ← hasta aqui. ")


if __name__ == "__main__":
    mostrar_anios_cumplidos()
