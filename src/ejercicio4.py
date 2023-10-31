#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre 
#por pantalla ordenados de menor a mayor.

def loteria(numeros):
    numeros_ganadores = []

    for numero in numeros:
        numeros_ganadores.append(int(numero))

    numeros_ganadores.sort()

    return numeros_ganadores

if __name__ == "__main__":
    entrada = input("Introduce los numeros ganadores de la loteria separados por espacios: ")
    numeros = entrada.split()
    numeros_ordenados = loteria(numeros)

    print("Numeros ganadores de la loteria primitiva ordenados de menor a mayor:")
    for numero in numeros_ordenados:
        print(numero)
