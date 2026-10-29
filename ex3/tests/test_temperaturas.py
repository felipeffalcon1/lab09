import pytest
from temperaturas import maior, dia_do_maior

def test_maior():
    assert maior([21, 25, 19, 30, 22]) == 30
    assert maior([18]) == 18
    assert maior([30, 21]) == 30
    assert maior([20, 20, 10]) == 20
    with pytest.raises(ValueError, match="^lista vazia$"):
        maior([])

def test_dia_do_maior():
    assert dia_do_maior([21, 25, 19, 30, 22]) == 3
    assert dia_do_maior([18]) == 0
    assert dia_do_maior([30, 21]) == 0
    assert dia_do_maior([30, 25, 30]) == 0
    with pytest.raises(ValueError, match="^lista vazia$"):
        dia_do_maior([])
