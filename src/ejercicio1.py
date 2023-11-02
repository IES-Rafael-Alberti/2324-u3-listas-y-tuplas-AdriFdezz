#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista y la muestre por pantalla.

def mostrar_asignaturas(asignaturas):
    resultado = "Asignaturas del curso:\n" + "\n".join(asignaturas)
    return resultado

if __name__ == "__main__":
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    resultado = mostrar_asignaturas(asignaturas)
    print(resultado)
