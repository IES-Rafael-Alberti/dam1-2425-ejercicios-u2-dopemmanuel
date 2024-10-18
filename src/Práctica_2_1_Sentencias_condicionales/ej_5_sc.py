"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""
def confirmar_edad_ingresos(age):
    """Condiciones"""
    from src.Práctica_2.1_Sentencias_condicionales.ej_1_sc.py import 
    

def main():
    """Variables"""
    while True:
        try:
            age = int(input("Cual es tu edad? → "))
            ingresos = float(input("De cuanto son tus ingresos? → "))
        except ValueError:
            print("ERROR 001: solo se permiten caracteres numericos.")

if __name__ == "__main__":
    main()