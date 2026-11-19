MAXIMO = 28  # LIMITE = 20 + D, D = 8 (matricula 1142644298)


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual < MAXIMO
