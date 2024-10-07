# JUEGO "Adivinanza del numero"
# Generaremos un número entre 1 y 10.
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. También poner el número de intentos requeridos.

# NOTA IMPORTANTE, estas dos lineas de abajo generan un numero aleatorio entre 1 y 10. 
# Pusimos el print para que vean que cada vez que ejecutan el codigo va a generarse un numero distinto.
# Mas adelante lo vamos a ver, asi que quedense tranquilos. 
# Solamente utilicen la variable numero para realizar el ejercicio.

import random

numero = random.randint(1,10)

cont_intentos = 0

while True:
    numero_random = int(input("adivina el numero entre 1 y 10: "))
    cont_intentos +=1
    if numero_random < numero:
        print("El numero es mayor: ")
    elif numero_random > numero: 
        print("El numero es menor: ")
    else:
        print(f"Adivinaste el numero en {cont_intentos} intentos")
        break
