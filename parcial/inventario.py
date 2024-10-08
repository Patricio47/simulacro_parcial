import os
os.system("cls")
def cargar_productos(inventario):
    cantidad = int(input("¿Cuantos productos deseas agregar? "))
    for _ in range(cantidad):
        nombre = input("Nombre del producto:")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad de productos: "))
        inventario.append([nombre, precio, cantidad])

def buscar_producto(inventario)->str:
    nombre = input("Nombre del producto a buscar: ").lower()
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            print(f"Nombre: {producto[0]}, precio: {producto[1]}, cantidad: {producto[2]}")
            return
    print("Producto no encontrado")

def ordenar_por_precio(producto):
    return producto[1]


def ordenar_inventario(inventario):
    if len(inventario) > 0:

        n = len(inventario)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if inventario[j][1] > inventario[j+1][1]:
                    inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    else:
        print(f"lista vacia") 
        
    for i in range(len(inventario)):
        
        nombre = inventario[i][0]
        precio = inventario[i][1]
        stock = inventario[i][2]
        
        print(f"producto: {nombre}, precio: {precio} y stock: {stock}  ")   

def encontrar_producto_mas_caro(inventario):
    producto_mas_caro = inventario[0]
    for producto in inventario:
        if producto > producto_mas_caro:
            producto_mas_caro = producto
    return producto_mas_caro

def encontrar_producto_mas_barato(inventario):
    producto_mas_barato = inventario[0]
    for producto in inventario:
        if producto < producto_mas_barato :
            producto_mas_barato = producto
    return producto_mas_barato

def mostrar_producto_mas_caro(inventario):
    producto_caro = encontrar_producto_mas_caro(inventario)
    print(f"Producto mas caro: {producto_caro}")

def mostrar_producto_mas_barato(inventario):
    producto_barato = encontrar_producto_mas_barato(inventario)
    print(f"Producto mas barato: {producto_barato}")

def mostrar_productos_caros(inventario):
    for producto in inventario:
        if producto[1] > 15000:
            print(producto)