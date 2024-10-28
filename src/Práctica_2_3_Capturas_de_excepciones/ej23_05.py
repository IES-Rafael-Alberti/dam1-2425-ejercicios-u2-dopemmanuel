""" 
Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
lance la excepción NameError con el mensaje, "Incorrect Password!!
"""

def saved_passwrd():
    """Variables y condiciones"""
    contrasenias =["python","kotlin","C++"]
    activation = True
    
    while activation:
        try:
            insertar = input("Ingresa la contraseña → ")

            insertar = str(insertar)

            if insertar not in contrasenias:
                raise NameError("Incorrect Password!!")
            else:
                print("Correct Password!!!")

            activation = False

        except NameError as e:
            print(e)

def main():
    """Funcion principal"""

    saved_passwrd()

if __name__ == "__main__":
    main()
