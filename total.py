def calculate_total(products):
    total_general = 0
    for product, details in products.items():
        name, price, quantity = details
        total = price * quantity
        print(f"Total por {quantity} unidades de {name}: {total}")
        total_general += total
    print(f"Total general: {total_general}")