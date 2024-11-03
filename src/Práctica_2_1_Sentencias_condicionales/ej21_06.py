"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
su nombre y sexo, y muestre por pantalla el grupo que le corresponde. 
"""
def determinar_grupo(nombre, genero):
    """↓ Si la letra H o la M dentro de la cadena dentro de la variable va primero """

    if genero == "M" and nombre < "M" or genero == "H" and nombre > "N":
        return "A"
    else:
        return "B"


def main():
    """Solo las variables de entrada y talvez un exeption:"""
    nombre = input("Ingrese su nombre: → ").upper()
    genero = input("Su genero? (H para hombre y M para mujer): → ")

    print(f"Perteneces al grupo {determinar_grupo(nombre, genero)}")

if __name__ == "__main__":
    main()
