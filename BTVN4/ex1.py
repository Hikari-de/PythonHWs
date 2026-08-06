def manage_inventory(inventory, new_products, remove_product):
    laptop_quantity = inventory.get("Laptop", 0)
    print("Laptop quantity:", laptop_quantity)

    inventory.update(new_products)

    removed = inventory.pop(remove_product, "Not found")
    print(f"Removed '{remove_product}':", removed)

    print("Products:", inventory.keys())

    return sum(inventory.values())


inventory = {
    "Laptop": 10,
    "Mouse": 50,
    "Monitor": 5
}

new_products = {
    "Keyboard": 20,
    "Mouse": 55
}

remove_product = "Monitor"

total = manage_inventory(inventory, new_products, remove_product)
print("Total quantity:", total)