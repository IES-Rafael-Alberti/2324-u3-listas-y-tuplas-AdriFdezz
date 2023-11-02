#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def producto_escalar(vector1, vector2):
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    return producto

if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]
    resultado = producto_escalar(vector1, vector2)
    
    print("El producto escalar es:", resultado)
