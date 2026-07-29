# Function to create delivery orders
def create_orders():
    orders = []

    orders.append(("Laptop", 2, 350))
    orders.append(("Mouse", 5, 20))
    orders.append(("Monitor", 3, 220))

    return orders


# Function to find high-value items
def high_value_orders(orders):
    high_value_items = []

    for item, quantity, price in orders:
        total_cost = quantity * price

        if total_cost > 500:
            high_value_items.append((item, total_cost))

    return high_value_items


# Main Program
orders = create_orders()
high_value_items = high_value_orders(orders)

print("Items with Total Cost Above 500:")
for item, total in high_value_items:
    print(f"{item}: {total}")