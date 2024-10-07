# Imprime la tabla de multiplicar de un número dado por el usuario, se debe utilizar el bucle while.
numero =  int(input("Ingrese un numero: "))
contador = 0
while contador < 11:
    print(f"{numero} x {contador} = {numero * contador}")
    contador +=1
