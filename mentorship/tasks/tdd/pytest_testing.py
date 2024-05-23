from main import add, dividir

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_dividir():
    assert dividir(1, 2) == 0.5
    assert dividir(0, 1) == 0
    assert dividir(-1, 1) == -1
    assert dividir(-1, -1) == 1