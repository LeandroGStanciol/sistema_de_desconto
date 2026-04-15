def calcular_desconto(valor_compra, percentual):
    
    if valor_compra <= 0:
        return "Erro"

    if percentual < 0 or percentual > 50:
        return "Erro"

    desconto = valor_compra * (percentual / 100)
    valor_final = valor_compra - desconto

    return round(valor_final, 2)


if __name__ == "__main__":
    print("Teste 1:", calcular_desconto(100, 10))
    print("Teste 2:", calcular_desconto(200, 50))
    print("Teste 3:", calcular_desconto(-10, 10))