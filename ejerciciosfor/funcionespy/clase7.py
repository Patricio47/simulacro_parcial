def inicializar_matriz(filas : int, columnas: int) -> list[list]:
    matriz = []
    for _ in range(filas):
        fila = [0]  * columnas
        matriz += [fila] 
    return matriz

matriz2x3 = inicializar_matriz(4,8)

for fila in matriz2x3:
    print(fila)