import os
os.system("cls")

def mostrar_menu()->int:
    print("1. Cargar producto")
    print("2. Buscar Producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto mas caro y mas barato")
    print("5. Mostrar productos con precios mayor a 15000")
    print("6. Salir")

def obtener_opcion() -> str:
    return input("Seleccione una opción: ")