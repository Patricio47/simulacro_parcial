import os
os.system("cls")
inventario = [
    # ["Laptop", 1500.00, 10],
    # ["Silla", 200.00, 50],
    # ["Libro", 15.00, 100],
    # ["Monitor", 300.00, 30]
]

def mostrar_menu()->bool:
    print("1. Cargar producto")
    print("2. Buscar Producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto mas caro y mas barato")
    print("5. Mostrar productos con precios mayor a 15000")
    print("6. Salir")

def cargar_productos(inventario):
    cantidad = int(input("¿Cuantos productos deseas agregar? "))
    for _ in range(cantidad):
        nombre = input("Nombre del producto:")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad de productos: "))
        inventario.append([nombre, precio, cantidad])

def buscar_producto(inventario):
    nombre = input("Nombre del producto a buscar: ")
    for producto in inventario:
        if producto == nombre.lower():
            print(f"Nombre: {producto[0]}, precio: {producto[1]}, cantidad: {producto[2]}")
            return
    print("Producto no encontrado")

def ordenar_por_precio(producto):
    return producto[1]

inventario.sort(key=ordenar_por_precio)
inventario = inventario[::-1]
def ordenar_inventario(inventario):
    for producto in inventario:
        print(producto)
    if inventario == []:
        print("Lista vacia:")

def encontrar_producto_mas_caro(inventario):
    producto_mas_caro = inventario
    for producto in inventario:
        if producto > producto_mas_caro:
            producto_mas_caro = producto
    return producto_mas_caro

def encontrar_producto_mas_barato(inventario):
    producto_mas_barato = inventario
    for producto in inventario:
        if producto < producto_mas_barato :
            producto_mas_barato = producto
    return producto_mas_barato

def mostrar_producto_mas_caro(inventario):
    producto_caro = encontrar_producto_mas_barato(inventario)
    print(f"Producto mas caro: {producto_caro}")

def mostrar_producto_mas_barato(inventario):
    producto_barato = encontrar_producto_mas_barato(inventario)
    print(f"Producto mas barato: {producto_barato}")

def mostrar_productos_caros(inventario):
    for producto in inventario:
        if producto > 15000:
            print(producto)
opcion = None
while opcion != "6":
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case "1":
            cargar_productos(inventario)
        case "2":
            buscar_producto(inventario)
        case "3":
            ordenar_inventario(inventario)
        case "4":
            mostrar_producto_mas_barato(inventario)
            mostrar_producto_mas_caro(inventario)
        case "5":
            mostrar_productos_caros(inventario)
        case "6":
            break
        case _: 
            print("Opcion no valida")