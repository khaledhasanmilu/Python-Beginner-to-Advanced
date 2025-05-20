def calculate_total(cart_items, tax_rate):
    """
    Calculate the total cost of items in a shopping cart including tax.

    Parameters:
    cart_items (list of tuples): Each tuple contains (item_name, price, quantity)
    tax_rate (float): Tax rate as a decimal (e.g., 0.07 for 7%)

    Returns:
    float: Total cost including tax
    """
    subtotal = 0
    for item in cart_items:
        name, price, quantity = item
        subtotal += price * quantity
    
    total = subtotal * (1 + tax_rate)
    return round(total, 2)

# Example usage:
shopping_cart = [
    ("Apple", 0.99, 3),
    ("Bread", 2.50, 1),
    ("Milk", 3.00, 2)
]

total_price = calculate_total(shopping_cart, tax_rate=0.07)
print("Total with tax: $", total_price)
