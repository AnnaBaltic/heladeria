sabores_helado = {
    "Chocolate": {"precio": 1500, "stock": 50},
    "Vainilla": {"precio": 1390, "stock": 50}
}

def agregar_nuevo_sabor():
    sabor = input("Ingrese el nombre del sabor: ")
    try:
        precio = int(input("Ingrese el precio del helado: "))
        stock = int(input("Ingrese la cantidad d los helados en stock: "))
    except ValueError:
        print("\nError: Ingrese valores numéricos para el precio y el stock.")
        return
    
    sabores_helado[sabor] = {"precio": precio, "stock": stock}
    print(f"\nEl nuevo sabor de helado '{sabor}' con precio $'{precio}' y stock '{stock}' unidades, fue agregado con éxito.")

def mostrar_sabores_disponibles():
    print("\nSabores disponibles:")
    for nombre, datos in sabores_helado.items():
        print(f"{nombre}: Precio ${datos['precio']}, Stock {datos['stock']} unidades.")


def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar un nuevo sabor de helado.")
        print("2. Mostrar los sabores de helados disponibles.")
        print("3. Salir.")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            agregar_nuevo_sabor()
        elif opcion == "2":
            mostrar_sabores_disponibles()
        elif opcion == "3":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")


if __name__ == "__main__":
    menu()