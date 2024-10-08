import os
from menu import *
from inventario import (
    cargar_productos,
    buscar_producto,
    ordenar_inventario,
    mostrar_producto_mas_caro,
    mostrar_producto_mas_barato,
    mostrar_productos_caros
)

os.system("cls")
inventario = [
    # ["Laptop", 1500.00, 10],
    # ["Silla", 200.00, 50],
    # ["Libro", 15.00, 100],
    # ["Monitor", 300.00, 30]
]

opcion = None
while opcion != "6":
    mostrar_menu()
    opcion = obtener_opcion()
    match opcion:
        case "1":
            cargar_productos(inventario)
        case "2":
            buscar_producto(inventario)
        case "3":
            ordenar_inventario(inventario)
        case "4":
            mostrar_producto_mas_caro(inventario)
            mostrar_producto_mas_barato(inventario)
        case "5":
            mostrar_productos_caros(inventario)
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")