from src.ejercicio13 import calcular_desviacion

def test_calcular_desviacion():
    muestra = "1,2,3,4,5"
    media, desviacion = calcular_desviacion(muestra)
    assert media == 3.0
    assert desviacion == 1.4142135623730951