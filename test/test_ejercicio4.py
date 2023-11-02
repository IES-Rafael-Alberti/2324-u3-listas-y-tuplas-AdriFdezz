from src.ejercicio4 import loteria

def test_loteria():
        numeros = [4, 2, 1, 3]
        resultado = [1, 2, 3, 4]
        assert loteria(numeros) == resultado