"""
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""


def evaluacion_puntuacion(puntos):
    """IFs para la puntuacion con dos variables iniciales para nivel y puntos:"""
    nivel = ""
    puntos = 0

    if puntos <= -1:
        print("no es... factible!!!")

    elif puntos == 0.0:
        nivel = "inaceptable"
        dinero = 0 * puntos

    elif puntos <= 0.4:
        nivel = "Aceptable"
        dinero = 2400 * puntos

    elif puntos >= 0.6:
        nivel = "Meritorio"
        dinero = 2400 * puntos
    else:
        print("Puntuacion no valida")
        return None

    total = f"Tu nivel de rendimiento es {nivel}, Recibiras {dinero} €"
    return total

def main():
    """Variables y condicion con exeption:"""

    Verdad = True

    while Verdad:
        try:
            puntos = float(input("Ingrese la puntuacion → "))
            evaluacion_puntuacion(puntos)

            asken = input("Quieres seguir con la puntuacion? (s/n) → ")
            if asken != "s":
                Verdad = False

        except ValueError:
            print("ERROR: eso no es un formato numerico...")

if __name__=="__main__":
    main()
