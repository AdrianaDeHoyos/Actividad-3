from product import get_product
from quantity import get_quantity
from total import calculate_total

def main():
    products = {}
    while True:
        name, price = get_product()
        if name is None:
            break
        quantity = get_quantity(name)
        products[name] = (name, price, quantity)
    
    calculate_total(products)

if __name__ == "__main__":
    main()
