def calculate_total_value(item):
    """Return the total value of an item (price * quantity)."""
    return item["price"] * item["quantity"]


def stock_status(quantity):
    """Categorize stock level based on quantity remaining."""
    if quantity == 0:
        return "Out of Stock"
    elif quantity < 5:
        return "Low Stock"
    elif quantity < 20:
        return "In Stock"
    else:
        return "Overstocked"


def get_item_from_user():
    """Ask the user for an item's details and return them as a dict."""
    name = input("Item name: ").strip()
    price = float(input("Price per unit: "))
    quantity = int(input("Quantity in stock: "))
    return name, {"price": price, "quantity": quantity}


def build_inventory():
    """Loop, letting the user add items until they choose to stop."""
    inventory = {}
    while True:
        name, item = get_item_from_user()
        inventory[name] = item

        again = input("Add another item? (y/n) > ").strip().lower()
        if again != 'y':
            break
    return inventory


def process_inventory(inventory):
    """Loop through inventory items, compute value and status for each."""
    results = {}
    for name, item in inventory.items():
        total_value = calculate_total_value(item)
        status = stock_status(item["quantity"])
        results[name] = {
            "quantity": item["quantity"],
            "total_value": round(total_value, 2),
            "status": status,
        }
    return results


def print_inventory_report(results):
    """Display a formatted report of inventory results."""
    print(f"\n{'Item':<12}{'Qty':<6}{'Value':<10}{'Status'}")
    print("-" * 40)
    for name, info in results.items():
        print(f"{name:<12}{info['quantity']:<6}${info['total_value']:<9}{info['status']}")


def total_inventory_value(results):
    """Sum up the total value across all items."""
    total = 0
    for info in results.values():
        total += info["total_value"]
    return total


if __name__ == "__main__":
    print("=== Inventory Builder ===\n")
    inventory = build_inventory()
    results = process_inventory(inventory)
    print_inventory_report(results)
    print(f"\nTotal inventory value: ${total_inventory_value(results):.2f}")
