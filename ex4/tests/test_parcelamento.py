import pytest
from parcelamento import parcela

def test_parcelamento():
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100, 0)
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100, 13)

    assert parcela(100, 1) == 100.0
    assert parcela(100, 3) == 33.33
    assert parcela(100, 4) == 25.5
    assert parcela(100, 12) == 9.83
