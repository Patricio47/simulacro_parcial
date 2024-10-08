COMISION = 50

#Precios
PRECIO_TAMANIO_C = 2000
PRECIO_TAMANIO_M = 3000
PRECIO_TAMANIO_G = 3700
TERMINAR = "TERMINAR"


contador_tamanio_chico = 0
contador_tamanio_mediano = 0
contador_tamanio_grande = 0
contador_pedidos = 0


"""Función que valida si una cadena es "C", "M" o "G" y devuelve la cadena. 
    Argumentos: string
    Returns: string
    """
def validar_tamanio (tamanio: str) -> str:
    while (tamanio!="C") and (tamanio!="M") and (tamanio!="G"):
        tamanio = tamanio.upper()
        tamanio = str(input("Incorrecto, ingrese C, M, G o terminar")).upper()
    return tamanio

""""Validamos que la cantidad de gustos ingresados este en el rango 1-4
    arg: int
    return: int
    """
def validar_gustos (cantidad: int) -> int:
    while not (0< cantidad <5):
        cantidad = int(input("Ingrese una cantidad de gustos entre 1 y 4: "))
    return cantidad

"""Funcion que toma un tamaño en str y retorna su precio sumándole una comisión 
    Args: str{tamanio}
    Return :float{importe+comision}
    """
def importe_total(tamanio: str) -> float:
    if tamanio == "C":
        importe = PRECIO_TAMANIO_C
    elif tamanio =="M":
        importe = PRECIO_TAMANIO_M
    else:
        importe = PRECIO_TAMANIO_G
    return(importe+COMISION)

def propiedades_gustos(cantidad: int):
    for i in range(cantidad):
        gusto = input("Ingrese el gusto que desee: ")
    
    return gusto

while True:
    tamanio = validar_tamanio(input("Ingrese el tamaño  C,M,G o terminar: ")).upper()

    while(tamanio != TERMINAR):
        if tamanio == "C":
            contador_tamanio_chico +=1
        elif tamanio =="M":
            contador_tamanio_mediano +=1
        else:
            contador_tamanio_grande +=1
        contador_pedidos +=1
        cantidad_gustos = validar_gustos(int(input("Ingrese la cantidad de gustos: ")))
        for gusto in range(cantidad_gustos):
            nombre_del_gusto = input("ingrese el nombre del gusto: ")