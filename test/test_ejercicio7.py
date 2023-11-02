from src.ejercicio7 import filtrar_abecedario

def test_filtar_abecedario():
        abecedario = list("abcdefghijklmnñopqrstuvwxyz")
        abecedario_filtrado = [letras for i, letras in enumerate(abecedario, start=1) if i % 3 != 0]
        resultado = filtrar_abecedario()
        assert resultado == abecedario_filtrado