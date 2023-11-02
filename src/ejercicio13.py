#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre 
#por pantalla su media y desviación típica.

def calcular_desviacion(muestra):
    numeros = [float(numero) for numero in muestra.split(",")]
    n = len(numeros)

    if n == 0:
        return 0, 0

    media = sum(numeros) / n
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    desviacion_tipica = (suma_cuadrados / n) ** 0.5

    return media, desviacion_tipica

if __name__ == "__main__":
    muestra = input("Introduce una muestra de numeros separados por comas: ")
    media, desviacion = calcular_desviacion(muestra)
    print("La media de la muestra es: " + str(media))
    print("La desviacion tipica de la muestra es: " + str(desviacion))
