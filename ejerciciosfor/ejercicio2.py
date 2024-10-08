# Calcula la suma de todos los números pares del 1 al 50 utilizando un bucle for.
for i in range (50):
    if i % 2 == 0:
        i += i
        print(i)