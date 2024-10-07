# Crear un programa que solicite 5 números mediante prompt. Calcular la
# suma acumulada y el promedio de los números ingresados.

contador = 0
suma = 0
promedio = 0

while contador <5:
    numeros = int(input("ingrese 5 numeros"))
    contador += 1
    suma += numeros
    promedio = suma / 5
print(suma)
print(promedio)
