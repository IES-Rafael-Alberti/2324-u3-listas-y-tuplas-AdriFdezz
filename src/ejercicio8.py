#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def palindromo(palabra):
    palabra = palabra.lower()
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    if palindromo(palabra):
        print("La palabra es un palindromo.")
    else:
        print("La palabra no es un palindromo.")

