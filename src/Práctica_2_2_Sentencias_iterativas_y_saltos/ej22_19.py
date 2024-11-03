""" 
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 
3-finalizar programa. A continuación, el usuario debe poder seleccionar 
una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, 
permitiendo volver a elegir. Si elige las opciones 1 ó 2 se 
imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión 
del menú y el programa finalizará.
"""
import os
def introducion():
    """Funcion para el titulo:"""
    print("=" * 80)

    print("             Este programa me sirve para crear un menu.... tendre que")
    print("                       inprovisar de manera inesperada.")

    print("=" * 80)

def clear_console():
    """Esta funcion permite limpiar la consola: """
    if os.name == 'nt':
        os.system('cls')

def menu_and_options():
    """EL menu"""
    options = {"1","2","3"}
    lista = "- Red Dead Redemtion 1 and 2 \n- Minecraft Dungeons \n- GoW and ragnarok"
    active = True
    while active:
        try:
            print("Bienvenido al menu!! elija un opcion:\n")
            print("1 - ⟪ Comenzar programa ⟫")
            print("2 - ⟪ Imprimir listado ⟫")
            print("3 - ⟪ Finalizar programa ⟫")
            print("\n")
            choose = input("Opcion ---⟫ ")

            clear_console()

            if choose not in options :
                raise ValueError("ERR0R: esa opcion no es valida.")

            if choose == "1":
                input("Programa iniciado...")
                print("\n")
                print("Hola usuario!! el programa te da la Bienvenida (☆▽☆)")
                print("\n")
                input("Presiona ↩ para ir al menu....")

                clear_console()

            elif choose == "2":
                print("Lista de apps:")
                print("\n")
                print(lista)
                print("\n")
                input("Presiona ↩ para ir al menu....")

                clear_console()
            else:
                if choose == "3":
                    input("ヾ(￣▽￣) Bye~Bye~")
                    active = False
                    clear_console()

        except ValueError as common:
            print(common)
            print("\n")
            input("Presione ↩ para volver al menu...")
            clear_console()

def main():
    """Funcion principal:"""

    clear_console()
    introducion()
    print("\n")
    input("Presione ↩  para continuar...")

    clear_console()

    menu_and_options()

if __name__ == "__main__":
    main()
