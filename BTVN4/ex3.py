products = [
    {
        "id": "SP01",
        "name": "Laptop",
        "category": "Electronics",
        "price": 15000000,
        "stock": 10
    },
    {
        "id": "SP02",
        "name": "Mouse",
        "category": "Accessories",
        "price": 200000,
        "stock": 50
    },
    {
        "id": "SP03",
        "name": "Phone",
        "category": "Electronics",
        "price": 12000000,
        "stock": 0
    },
    {
        "id": "SP04",
        "name": "Keyboard",
        "category": "Accessories",
        "price": 800000,
        "stock": 15
    }
]

electronics = list(
    filter(lambda product: product["category"] == "Electronics", products)
)
print(electronics)

out_of_stock = list(
    filter(lambda product: product["stock"] == 0, products)
)
print(out_of_stock)

product_names = list(
    map(lambda product: product["name"], products)
)
print(product_names)

promotions = list(
    map(
        lambda product: f"Free 100k voucher for buying {product['name']}",
        filter(lambda product: product["price"] >= 1000000, products)
    )
)

print(promotions)