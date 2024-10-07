inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30]
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
        nombre = input("Nommbre del producto: ")
        precio = float(input("Nombre del producto: "))
        cantidad = int(input("Cantidad de productos: "))
        inventario.append([nombre, precio, cantidad])

def buscar_producto(inventario):
    nombre = input("Nombre del producto a buscar: ")
    for producto in inventario:
        if producto[0].lower() 