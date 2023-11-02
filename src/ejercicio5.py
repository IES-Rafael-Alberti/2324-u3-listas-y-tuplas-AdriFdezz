#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

def numeros_inversos():
    numeros = list(range(1, 11))
    numeros_invertidos = ','.join(str(numero) for numero in reversed(numeros))
    return numeros_invertidos

if __name__ == "__main__":
    numeros_ordenados = numeros_inversos()
    print(numeros_ordenados)
