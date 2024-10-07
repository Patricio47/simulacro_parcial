def fibonacci_iter(numero):
    if numero == 1:
        resultado = 1
        return resultado
    if numero == 0:
        resultado = 0
        return resultado
    else:
        resultado = fibonacci_iter(numero -1) + fibonacci_iter(numero -2)
        return resultado


resultado = fibonacci_iter(6)
print(resultado)

