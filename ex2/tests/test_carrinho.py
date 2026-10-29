from carrinho import total_com_desconto

def test_carrinho():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0
    assert total_com_desconto([10, 10, 10]) == 30.0
    assert total_com_desconto([10, 10, 10, 10]) == 39.0
    assert total_com_desconto([]) == 0.0
    assert total_com_desconto([10.555, 10.555, 10.555, 10.555]) == 41.16
