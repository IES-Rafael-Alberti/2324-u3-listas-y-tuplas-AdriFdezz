from src.ejercicio1 import mostrar_asignaturas

def test_mostrar_asignaturas():
        asignaturas = ["Matematicas", "Fisica", "Lengua"]
        resultado = "Asignaturas del curso:\nMatematicas\nFisica\nLengua"
        assert mostrar_asignaturas(asignaturas) == resultado