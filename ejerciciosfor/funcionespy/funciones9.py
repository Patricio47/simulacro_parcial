# 1. Importar la librería de aleatoriedad random:
# 1. import random # arriba de todo el código
# 2. Hacer una función que se llame tirarLaMoneda y reciba como parámetro un booleano 
# llamado estaCargada.
# 3. Llamar a la función random.random() la cual te devuelve un valor entre 0 y 1. Este valor va 
# a ser la probabilidad de cara (guardarlo en una variable)
# 4. Si el parámetro estaCargada es True:
# 1. Si el valor de probabilidad de cara es mayor a 0.2 retorno “CARA”
# 2. Sino, retorno “CRUZ”
# 5. En otro caso:
# 1. Si el valor de probabilidad de cara es mayor a 0.5 retorno “CARA”
# 2. Sino, retorno “CRUZ”
# Ejemplos de uso y respuesta:
# tirarLaMoneda(True) # tiene más probabilidad de retornar “CARA” que “CRUZ” 
# porque decimos que es una ‘moneda cargada’.
# tirarLaMoneda(False) # tiene la misma probabilidad de retornar “CARA” que 
# “CRUZ”
# PLUS
# Envolver todo el ejercicio dentro de un bucle hasta que el usuario ingrese un número negativo
import random 


def tirarLaMoneda(estaCargada):
        probabilidad = random.random()
        if estaCargada:
            if probabilidad > 0.2:
                return"CARA"
            else:
                return"CRUZ"
        else:
            if probabilidad > 0.5:
                return "CARA"
            else:
                return"CRUZ"

while True:
    numero = int(input("Ingrese un número (negativo para salir): "))
    if numero < 0:
        print("Número negativo ingresado. Saliendo del programa.")
        break
    estaCargada = input("¿La moneda está cargada? (sí/no): ")
    resultado = tirarLaMoneda(estaCargada)
    print(f"Resultado: {resultado}")

