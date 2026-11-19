MAXIMO = 28  # LIMITE = 20 + D, D = 8 (matricula 1142644298)


def desconto_valido(percentual):
    if not isinstance(percentual, int) or isinstance(percentual, bool):
        return False
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
