def piramide_numeros(n):
    """Genera una pirámide de números con secuencia descendente y ascendente."""
    for i in range(n, 0, -1):
        linea = ""
        for j in range(i, 0, -1):
            linea += str(j)
        print(linea)


    for i in range(n + 1):
        linea = ""
        for j in range(i + 1):
            linea += str(j)
        print(linea)


num_filas = int(input("Introduce el número máximo para la pirámide: "))
piramide_numeros(num_filas)
