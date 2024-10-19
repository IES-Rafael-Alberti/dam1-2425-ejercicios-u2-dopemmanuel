"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""
def ingredientes_pizza(veggy):
    """Condiciones para los ingredientes:"""
    if veggy =="si":
        print("Ingredientes vegetarianos disponibles: Pimiento y Tofu")
        ingredients = input("Elige un ingrediente (Pimiento o Tofu): ").lower()

        if ingredients in ("pimiento", "tofu"):
            print(f"Pizza vegetariana con Mozzarella, Tomate y {ingredients}." )
        else:
            print("El ingrediente no esta disponible")
    else:
        print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón")
        ingredients = input("Elige un ingrediente (Peperoni, Jamón o Salmón): ").lower()

        if ingredients in ("Peperoni", "jamon", "Salmon"):
            print(f"Pizza no vegetariana con Mozzarella, Tomate y {ingredients}")
        else:
            print("Ese Ingrediente no esta en la lista")

def main():

    """Variables con condiciones"""
    veggy = input("quieres una pizza vegetariana? (Yes/Not)")

    if veggy in ("si", "no"):
        ingredientes_pizza(veggy)
    else:
        print("Respuesta no válida, por favor responde con 'si' o 'no'.")

if __name__ == "__main__":
    main()
