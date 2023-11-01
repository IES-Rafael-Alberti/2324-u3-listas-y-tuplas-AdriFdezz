#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

def contar_vocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    cuenta_vocales = [0, 0, 0, 0, 0]

    for letra in palabra:
        letra = letra.lower()
        if letra in vocales:
            posicion = vocales.index(letra)
            cuenta_vocales[posicion] += 1

    return cuenta_vocales

if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    cuenta_vocales = contar_vocales(palabra)
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vocales)):
        print("La vocal " + vocales[i] + " aparece " + str(cuenta_vocales[i]) + " veces")

