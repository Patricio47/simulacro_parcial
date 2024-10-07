# Escribir un programa que muestre el eco de todo lo que el usuario 
# introduzca hasta que el usuario escriba "salir" que terminará.

entradas = []

while True:
    entrada = input("Ingrese una palabra o ´salir´ para terminar ")
    if entrada.lower() == "salir":
        break
    entradas.append(entrada)

for entrada in entradas:
    print(entrada)