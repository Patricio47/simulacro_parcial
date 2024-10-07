# from os import system
# system("cls")
# # Desarrollar una función que invierte el orden de los caracteres en una cadena. Utilizar Slicing

# # def invertir_cadena(cadena)->str:
# #     return cadena[::-1]
# # """" pasamos por parametro una cadena y la retornamos dada vuelta por slicing xD"""

# # mensaje = "loco"
# # mensaje_invertido = invertir_cadena(mensaje)

# # print(f"el mensaje sin invertir es: {mensaje} y el mensaje invertido es: {mensaje_invertido}")

# # Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.
# # 1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada.
# # 2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
# # 3. Extraer la nota y almacenarla en una variable llamada nota.
# # 4. Extraer la materia y almacenarla en una variable llamada materia. 
# # 5.  Mostrar por pantalla la siguiente estructura, usando la concantenación de cadenas: NOMBRE APELLIDO ha sacado un NOTA en MATERIA


# # cadena = "acitametaM ,5.8 ,otipeP ordeP"
# # def cadena_volteada(cadena)->str:
# #     return cadena[::-1]

# # cadena_dadavuelta = cadena_volteada(cadena)
# # nombre_alumno = cadena_dadavuelta.split()[0] + " " + cadena_dadavuelta.split()[1][:-1]
# # nota = cadena_dadavuelta.strip()[14:17]
# # materia = cadena_dadavuelta.split()[3]

# # print(cadena_dadavuelta)
# # print(nota)
# # print(f"{nombre_alumno} ha sacado un {nota} en {materia}")

# # def mostrar_resultado(nombre_alumno, nota, materia):
# #     resultado = f"{nombre_alumno} ha sacado un {nota} en {materia}"
# #     print(resultado)

# # mostrar_resultado(nombre_alumno, nota, materia)

# # Escribir un programa que imprima un patrón como el siguiente teniendo
# # como input un 5 (puede ser en Código o diagrama):

# # 123454321
# # 1234 4321
# # 123   321
# # 12     21
# # 1       1  

# # def patron(n):
# #     for i in range(n):
# #         for j in range(1,n-i +1):
# #             print(j, end="")
# #         if i >0:
# #             print(" "* (2*i -1), end="")
# #         for q in range(n-i,0, -1):
# #             if q == n:
# #                 continue
# #             print(q, end="")
            
# #         # for q in range(1,n-i -1):
# #         #     print(q, end="")
# #         print()

# # patron(5)

# # Desarrollar una función que convierta los elementos de lista_peli en una cadena y muestre:
# # ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento

# # Desarrollar una función que convierta los elementos de lista_peli en una cadena y muestre:
# # ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento

# # def recomendar_peliculas(lista_peli):
# #     for sublista in lista_peli:
# #         if len(sublista) == 1:
# #             cadena = f'Se recomienda ver "{sublista[0]}"'
# #         elif len(sublista) == 2:
# #             cadena = f'Se recomienda ver "{sublista[0]}" y "{sublista[1]}"'
# #         else:
# #             cadena = f'Se recomienda ver ' + ', '.join(f'"{peli}"' for peli in sublista[:-1]) + f' y "{sublista[-1]}"'
# #         print(cadena)

# # # Lista de películas
# # lista_peli = [
# #     ["Matrix", "El Padrino", "Titanic"],
# #     ["Forrest Gump", "Pulp Fiction", "Gladiador"],
# #     ["Blade Runner", "El Rey León", "Volver al Futuro"],
# #     ["La La Land", "El Gran Lebowski", "Blade Runner"],
# #     ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
# #     ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
# #     ["Titanic", "Star Wars", "El Señor de los Anillos"],
# #     ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
# #     ["Forrest Gump", "The Godfather", "Goodfellas"],
# #     ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
# # ]

# # # Llamar a la función
# # recomendar_peliculas(lista_peli)


# """
# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro. Si la lista tiene un 0, se debera omitir.

# Caso de uso:
# El resultado sera 8.
# """
# # lista_numeros = [4, 0, 2]

# # def producto_sin_cero(lista):
# #     producto = 1
# #     for numero in lista:
# #         if numero != 0:
# #             producto *= numero
# #     return producto

# # resultado = producto_sin_cero(lista_numeros)
# # print(resultado)


# """
# Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000.
# Calcular el porcentaje de personas que superan el salario promedio de estos mismos.
# """

# import random
# def generar_sueldos():
#     lista_aleatoria = [random.randint(35000, 1250000) for _ in range(10)]
#     return lista_aleatoria

# def calcular_promedio(lista_aleatoria):
#     suma = 0
#     sueldo_alto = 0
#     for numero in lista_aleatoria:
#         suma += numero
#         if numero > lista_aleatoria:
#             sueldo_alto = lista_aleatoria[numero]


#     promedio = suma /10
#     return promedio, sueldo_alto

# def calcular_porcentaje(promedio):
#     pass

# sueldos = generar_sueldos()
# promedio = calcular_promedio(sueldos)


# print(f"los sueldos son: {sueldos} y el promedio es: {promedio}")
