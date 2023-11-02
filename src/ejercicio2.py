#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
#sobre cada una de las asignaturas de la lista.

def mostrar_asignaturas(asignaturas):
    mensajes = []
    for asignatura in asignaturas:
        mensajes.append("Yo estudio " + asignatura)
    return mensajes

if __name__ == "__main__":
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    mensajes = mostrar_asignaturas(asignaturas)
    
    for mensaje in mensajes:
        print(mensaje)
