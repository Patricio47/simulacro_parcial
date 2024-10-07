# Realizar una función llamada par_o_impar:

# 1-Recibirá un número por parámetro
# 2-Imprimirá Par si el número es par
# 3-Imprimirá Impar si el número es impar
# 4-Si se ingresa algo que no sea número debe indicar 
# que se ingrese un número. (Para pensar un poco más)


def par_o_impar(numero):
    try:
        numero = int(numero)
        if numero %2 == 0:
            print(f"el numero es par: {numero}")
        else:
            print(f"el numero es impar: {numero}")
    
    except ValueError:
        print("ingrese un numero")
    


par_o_impar(4)
par_o_impar(5)
par_o_impar("a")
