def numero_ntero(numr):

    """OK"""    
    entero = ""
    for inicial in range(1, int(numr) + 1):
        entero += str(inicial) + ","

    return entero[:-1]

def main():
    """OKS"""
    numr = input("Ingresa un numero entero → ")
    numr = int(numr)

    print(numero_ntero(numr))

if __name__ == "__main__":
    main()