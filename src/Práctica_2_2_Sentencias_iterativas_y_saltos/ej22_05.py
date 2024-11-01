""" 
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""
def informacion():
    nostrings = True
    button = True
    while button:
        try:
            user = input("Ingrese un usuario: → ")
            amount = input(f"{user}, Ingresa la cantidad a invertir: → ")
            nostrings = False
            interest = input(f"Ok {user}, ahora ingresa el Interes anual: → ")

            amount = float(amount)
            interest = int(interest)

        except ValueError as e:
            if



def main():

if __name__ == "__main__":
    pass
    main()