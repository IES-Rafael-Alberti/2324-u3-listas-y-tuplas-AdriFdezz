from src.ejercicio3 import calcular_notas

def test_calcular_notas():
        asignaturas = ["Matematicas", "Fisica", "Lengua"]
        notas = ["5", "6", "7"]
        resultado = ["En Matematicas has sacado 5", "En Fisica has sacado 6", "En Lengua has sacado 7"]
        assert calcular_notas(asignaturas, notas) == resultado