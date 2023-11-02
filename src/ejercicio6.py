#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def calcular_asignaturas_repetir(asignaturas, notas):
    asignaturas_repetir = []

    for i, asignatura in enumerate(asignaturas):
        if notas[i] < 5:
            asignaturas_repetir.append(asignatura)

    return asignaturas_repetir

if __name__ == "__main__":
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    notas = []

    for asignatura in asignaturas:
        nota = int(input("Introduce la nota para " + asignatura + ": "))
        notas.append(nota)

    asignaturas_a_repetir = calcular_asignaturas_repetir(asignaturas, notas)

    if asignaturas_a_repetir:
        print("Debes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_a_repetir:
            print(asignatura)
    else:
        print("Has aprobado todas las asignaturas")
