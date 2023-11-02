from src.ejercicio10 import precios_mayor_menor

def test_precio_mayor_menor():
        precios = [10, 20, 30, 40, 50]
        resultado = precios_mayor_menor(precios)
        assert resultado == (10, 50)