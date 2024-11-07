def get_product():
    product = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if product.lower() == "fin":
        return None, None
    price = float(input(f"Ingrese el precio unitario de {product}: "))
    return product.upper(), price
