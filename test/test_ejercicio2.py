from src.ejercicio2 import mostrar_asignaturas

def test_mostrar_asignaturas():
        asignaturas = ["Matematicas", "Fisica", "Lengua"]
        resultado = ["Yo estudio Matematicas", "Yo estudio Fisica", "Yo estudio Lengua"]
        assert mostrar_asignaturas(asignaturas) == resultado