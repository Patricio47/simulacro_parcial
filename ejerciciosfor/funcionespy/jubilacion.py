
# # Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion)
# # y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos
# # (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
# #  y terminar el programa. Si todos los datos fueron bien ingresados,
# # el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas,
# # los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades.
# # Determinar mediante funciones si una persona puede o no jubilarse.

FEMENINO = "F"
MASCULINO = "M"
NOBINARIO = "X"
EDAD_MINIMA = 1
EDAD_MAXIMA = 99
def validarEdad(edad):
    if edad<EDAD_MINIMA or edad>EDAD_MAXIMA:
        print("Edad invalida")
    return 0
    
def validarGenero(genero):
    if genero !=FEMENINO or genero!=MASCULINO or genero!=NOBINARIO:
        print("Genero invalido")
    return 0
def jubilar(edad,genero):
    edad_m = 65
    edad_f = 60
    edad_x = 62.5
    jubilarse = "usted puede jubilarse"
    no_jubilarse = "usted no puede jubilarse"
    
    if genero == MASCULINO:
        if edad >=edad_m:
            return jubilarse
        else:
            return no_jubilarse
    elif genero == FEMENINO:
        if edad >= edad_f:
            return jubilarse
        else:
            return no_jubilarse
    elif genero == NOBINARIO:
        if edad >= edad_x:
            return jubilarse
        else:
            return no_jubilarse
while True:

    edad = int(input("Ingrese su edad: "))
    validar_edad = validarEdad(edad)

    if validar_edad:
        print(validar_edad)
        break
    else:
        genero = input("Ingrese su genero: ").upper()
        error_genero = validarGenero(genero)
        if error_genero:
            print(error_genero)
            break
        else:
            se_jubila = jubilar(edad,genero)
            print(se_jubila)
            break
        

