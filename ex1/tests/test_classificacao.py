import pytest
from classificacao import classificar_aluno

def test_classificacao():
    assert classificar_aluno(8.0, 80) == "Aprovado"
    assert classificar_aluno(7.0, 75) == "Aprovado"
    assert classificar_aluno(6.9, 75) == "Recuperacao"
    assert classificar_aluno(5.0, 75) == "Recuperacao"
    assert classificar_aluno(4.9, 75) == "Reprovado"
    assert classificar_aluno(3.0, 90) == "Reprovado"
    assert classificar_aluno(8.0, 74) == "Reprovado por falta"

    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(-0.1, 80)
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(10.1, 80)
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8.0, -1)
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8.0, 101)
