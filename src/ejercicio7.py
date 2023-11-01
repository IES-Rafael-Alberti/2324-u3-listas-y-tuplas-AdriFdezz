#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
#posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def filtrar_abecedario():
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")
    abecedario_filtrado = [letra for i, letra in enumerate(abecedario, start= 1) if i % 3 != 0]
    return abecedario_filtrado

if __name__ == "__main__":
    abecedario_filtrado = filtrar_abecedario()
    print(abecedario_filtrado)
