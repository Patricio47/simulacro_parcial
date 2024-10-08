# Solicitar al usuario ingresar los tres lados de un triángulo e indicar de qué tipo es:
# Isósceles: 2 lados iguales
# Equilátero: 3 lados iguales
# Escaleno: 0 lados iguales
triangulo = ""

for i in range (1,4):
    lado = int(input("ingrese los 3 lados de un triangulo: "))
    if i == 1:
        ladoa = lado
    elif i == 2:
        ladob = lado
    else:
        ladoc = lado

if ladoa == ladob and ladoa == ladoc:
    triangulo = "equilatero"
elif ladoa == ladob and ladoa != ladoc:
    triangulo = "isosceles"
else:
    triangulo = "escaleno"

print(f"El triangulo es: {triangulo}")    
