#Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla 
#el menor y el mayor de los precios.

def precios_mayor_menor(precios):
    menor_precio = min(precios)
    mayor_precio = max(precios)
    
    return menor_precio, mayor_precio

if __name__ == "__main__":
    precios = [50, 75, 46, 22, 80, 65, 8]
    menor, mayor = precios_mayor_menor(precios)
    
    print("El menor precio es:", menor)
    print("El mayor precio es:", mayor)
