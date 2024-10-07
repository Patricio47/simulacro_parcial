# Escribe una función llamada celsius_a_fahrenheit que tome una temperatura 
# en grados Celsius como argumento y devuelva su equivalente en grados Fahrenheit.

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) +32
celsius= 25
fahrenheit = celsius_a_fahrenheit(celsius) 
print(f"{celsius}°C es igual a {fahrenheit}°F")
