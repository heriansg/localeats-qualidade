def pedido_atingiu_valor_minimo(valor_pedido: float) -> bool:
    """Verifica se o valor do pedido atinge o mínimo de R$ 30,00."""
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30.0