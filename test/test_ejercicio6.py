from src.ejercicio6 import calcular_asignaturas_repetir

def test_calcular_asiganturas_repetir():
        asignaturas = ['Matematicas', 'Fisica', 'Lengua']
        notas = [7, 4, 6]

        result = calcular_asignaturas_repetir(asignaturas, notas)

        assert result == ['Fisica']