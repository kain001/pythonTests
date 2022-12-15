def sumar(a, b):
    result = a + b
    return result


def restar(a, b):
    result = a - b
    return result


def multiplicar(a, b):
    result = a * b
    return result


def dividir(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = 0
        return result
    except TypeError:
        result = "Result not supported"
        return result


def test_function():
    assert sumar(2, 2) == 4
    assert restar(2, 2) == 0
    assert multiplicar(2, 2) == 4
    assert dividir(4, "hola") == "Result not supported"
