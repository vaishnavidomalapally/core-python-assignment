
def calculate_total(cart_items):
    if not cart_items:
        return 0

    total = sum(cart_items.values())
    
    
    if len(cart_items) > 5:
        total -= total * 0.10
    return total



cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print("Total Price:", calculate_total(cart_items))
