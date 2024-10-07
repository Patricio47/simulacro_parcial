import os
clear = lambda: os.system('cls')
clear()

contador_iter = 0
contador_perro = 0
contador_gato = 0
contador_hamster = 0
contador_perro_gato = 0
acum_mascota_parasito = 0
contador_parasitos = 0
flag_mascota_joven = 1
diag_mascota_joven = ""
edad_mascota_joven = 0

while(contador_iter < 2):
    edad = int(input("Ingrese la edad: "))
    while(edad<1 or edad>20):
        edad = int(input("Ingrese la edad: "))
    tipo = input("Ingrese el tipo: (gato) (perro) (hamster)")
    while(tipo!="gato" and tipo!="perro" and tipo!="hamster"):
        tipo = input("Ingrese el tipo: (gato) (perro) (hamster)")
    peso = int(input("Ingrese el peso (mayor que 0kg)"))
    while(peso<0):
        peso = int(input("Ingrese el peso (mayor que 0kg)"))
    diagnostico = input("ingrese su diagnostico (digestivos) (parasitos) (infeccion)")
    while(diagnostico!="digestivos" and diagnostico!="parasitos" and diagnostico!="infeccion"):
        diagnostico = input("ingrese su diagnostico (digestivos) (parasitos) (infeccion)")
    vacuna = input("ingrese si tiene vacuna: ")
    while(vacuna!="si" and vacuna !="no"):
        vacuna = input("ingrese si tiene vacuna: ")

    if((tipo =="gato" or tipo == "perro") and vacuna=="no" and peso>9 and peso<21):
        contador_perro_gato +=1
    match tipo:
        case "gato":
            contador_gato +=1
        case "perro":
            contador_perro +=1
        case _:
            contador_hamster+=1

    if(diagnostico =="infeccion"):
        if(flag_mascota_joven==1):
            flag_mascota_joven=0
            diag_mascota_joven = diagnostico
            edad_mascota_joven = edad
        if(edad<edad_mascota_joven):
            diag_mascota_joven = diagnostico
            edad_mascota_joven = edad

    if(diagnostico=="parasitos"):
        acum_mascota_parasito += peso
        contador_parasitos +=1
    contador_iter +=1
    #Fin del while
tipo_mascota_max = "hamster"
if(contador_perro>contador_hamster and contador_perro>contador_gato):
    tipo_mascota_max = "perro"
elif(contador_gato>contador_hamster):
    tipo_mascota_max = "gato"

if(contador_perro>0):
    procentaje_perro= contador_perro * 100 / contador_iter
else:
    procentaje_perro="no se ingresaron perros"
if(contador_gato>0):
    porcentaje_gato= contador_gato * 100 / contador_iter
else:
    porcentaje_gato = "no se ingresaron gatos"
if(contador_hamster>0):
    procentaje_hamster= contador_hamster * 100 / contador_iter
else:
    procentaje_hamster = "no se ingresaron hamsters"

if(contador_parasitos>0):
    promedio_peso = acum_mascota_parasito / contador_parasitos
else:
    promedio_peso = "no se puede hacer promedio"

print(f"Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg es: {contador_perro_gato}")
print(f"El tipo de mascota más ingresada con parásitos es: {tipo_mascota_max}")
print(f"Edad y diagnóstico de la mascota más joven que se presentaron con una infección es: {edad_mascota_joven} y {diag_mascota_joven}")
print(f"Porcentaje de gatos es: {porcentaje_gato} de perro: {procentaje_perro} de hamsters: {procentaje_hamster}")
print(f"Promedio de pesos de mascotas con parásitos es: {promedio_peso}")