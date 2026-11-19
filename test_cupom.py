from cupom import MAXIMO, desconto_valido


def test_t1_aceita_percentual_exatamente_no_limite():
    # Preparar
    percentual = MAXIMO
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is True


def test_t2_rejeita_percentual_acima_do_limite():
    # Preparar
    percentual = MAXIMO + 1
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False


def test_t3_rejeita_percentual_zero():
    # Preparar
    percentual = 0
    # Agir
    resultado = desconto_valido(percentual)
    # Verificar
    assert resultado is False
