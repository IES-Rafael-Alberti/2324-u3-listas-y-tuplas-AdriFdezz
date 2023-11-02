#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
#En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> 
#cada una de las correspondientes notas introducidas por el usuario.

def calcular_notas(asignaturas, notas):
    resultados = []
    for asignatura in range(len(asignaturas)):
        resultados.append("En " + asignaturas[asignatura] + " has sacado " + notas[asignatura])
    return resultados

if __name__ == "__main__":
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] 
    notas = []

    for asignatura in asignaturas:
        nota = input("Introduce la nota para " + asignatura + ": ")
        notas.append(nota)

    resultados = calcular_notas(asignaturas, notas)
    
    for resultado in resultados:
        print(resultado)
