from src.ejercicio11 import producto_escalar

def test_producto_escalar():
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        assert producto_escalar(vector1, vector2) == 32