import os

def pedir_num():
    nostring = True
    test = True
    while test:
        try:
            num = input("Ingresa un número entero → ")
            nostring = False
            if num == "":
                print("Bye Bye...")
                return None

            if "." in num:
                raise ValueError("Nada de decimales")

            nostring = True
            num = int(num)
            nostring = False

            test = False

        except ValueError as e:
            if nostring:
                print("ERROR: No debería ser letra.")
            else:
                print(e)
    return num

def funcionar(num):
    if num is None:
        return

    if num < 0: 
        for i in range(-1, num - 2, -2):
            fila = ""
            for n in range(i, -2, 2):
                fila = str(n) + " " + fila
            print(fila.strip())
    else:
        for i in range(1, num + 1, 2):
            fila = ""
            for n in range(i, 0, -2):
                fila = str(n) + " " + fila
            print(fila.strip())

def clear_console():
    if os.name == 'nt':
        os.system('cls')

def main():
    num = pedir_num()
    funcionar(num)

    continuar = input("Presiona Para continuar.....")
    if continuar == "":
        clear_console()
        return pedir_num()


if __name__ == "__main__":
    main()
