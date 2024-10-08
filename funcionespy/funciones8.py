# Escribe una función llamada  que reciba una altura y el peso
# e indique el indice de masa CORPORAL (IMC) de una persona.
# Peso inferior al normal	imc < de 18.5
# Normal imc entre 18.5 – 24.9
# Peso superior al normal  imc entre 25.0 – 29.9
# Obesidad	imc > de 30.0


def calculo_de_imc(peso, altura):
    return peso / (altura ** 2)

altura = float(input("Ingrese su altura"))
peso = int(input("ingrese su peso"))

imc = calculo_de_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

if imc <= 18.5:
    print("peso inferior al normal")
elif imc >=18.5 and imc <=24.9:
    print("Peso normal")
elif imc >=25 and imc <=29.9:
    print("Peso superior al normal")
elif imc > 30:
    print("obesidad")


