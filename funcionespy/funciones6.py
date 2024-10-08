# Escribe una función llamada calculadora que tome tres argumentos:
# dos números y un operador (+, -, *, /). La función debe realizar 
# la operación correspondiente y devolver el resultado.
# Deben tener en cuenta el error de la division por 0 y que no ocurra.

# Extra: se puede realizar un breve menu en donde el usuario puede
# seleccionar:
#  1. Utilizar calculador
#  2. Salir
# si el usuario no ingresa 1 o 2, mostrarle un mensaje que no es una
# opcion correcta.

def calculadora (num1,num2,operador):

    if operador == "+":
        calcular = num1 + num2
        return calcular
    elif operador == "-":
        calcular = num1 - num2
        return calcular
    elif operador == "*":
        calcular = num1 * num2
        return calcular
    elif operador == '/':
        if num2 == 0:
            return "Error: Division por cero no permitida."
    else:
        calcular = num1 / num2
        return calcular


def menu(): 
    while True:
        print("Menú: \n 1. Utilizar calculadora \n 2. Salir")
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            operador = input("Ingrese el operador (+, -, *, /): ")
            resultado = calculadora(num1, num2, operador)
            print(f"Resultado: {resultado}")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("No es una opcion correcta, elija entre 1 o 2") 


menu()