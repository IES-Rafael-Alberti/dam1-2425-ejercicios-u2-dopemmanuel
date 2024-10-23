"""Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña 
e imprima por pantalla si la contraseña introducida por el 
usuario coincide con la guardada en la variable sin tener en 
cuenta mayúsculas y minúsculas."""

def contraseña(usuario, passrwd, passwords):

    """Condicion para las contraseñas que si las contraseñas en passwords
    no estan en el input del passwrd debe retornar a false, sino va a imprimir
    un saludo con el nombre de usuario."""
    if passrwd not in passwords:
        return False
    else:
        print(f"Bienvenido {usuario}!!")
        return True

def confirmar_contraseña(correcto):
    """Condicion para confirmar que la coondicion que esta dentro de la variable
    def contraseña(usuario, passrwd, passwords) debe ser true, la funcion se coloco
    en la variable correcto para ser confirmada en el main, y la variable correcto
    se esta usando en la funcion def confirmar_contraseña(correcto), que se usara para la condicion: """

    if correcto is not True:
        return False
    else:
        return True

def main():

    """Las variables con los datos(Passwords, usuario y passwrd).

    Y una variable extra que almacenara el def contraseña(usuario, passrwd, passwords),
    lo cual la variable sera usada en def confirmar_contraseña(correcto) para 
    confirmar si es True.
    
    Despues condicionar con un while para hacer un bucle y alegorarle
    que si la funcion confirmar_contraseña(correcto) no es igua igual a
    contraseña(usuario, passwrd, passwords) que inprima que es incorrecta
    y que pida los datos otra vez. 
    """

    passwords = ["UbuntuLinux",
                 "contraseña",
                 "hello world!!",
                 "python",
                 "biblioteca"
                 ]
    usuario = input("Nombre de usuario → ")
    passwrd = input("Contrasena → ")

    correcto = contraseña(usuario, passwrd, passwords)

    while confirmar_contraseña(correcto) == contraseña(usuario, passwrd, passwords):

        print("La contraseña es incorrecta")
        usuario = input("Nombre de usuario → ")
        passwrd = input("Contrasena → ")

if __name__ ==  "__main__":
    main()
